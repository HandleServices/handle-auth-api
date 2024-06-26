from typing import Annotated, Callable

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.utils import get_db_session
from src.infra.auth import AuthResponse, token_handler
from src.infra.exceptions import AlreadyExistsError
from src.use_cases.register import repository
from src.use_cases.register.models import RegisterSchema
from src.use_cases.register.models.validate_credentials import ValidateCredentialsSchema, ValidateFieldSchema
from src.use_cases.register.repository import create_expedient, check_availability

register_router = APIRouter(tags=['Register'])


@register_router.post('')
async def register(
        schema: RegisterSchema,
        session: Annotated[AsyncSession, Depends(get_db_session)]
) -> AuthResponse:
    try:
        worker_id = await repository.create_worker(schema, session)

        await repository.create_worker_login(worker_id, schema.password, session)

        for expedient in schema.expedient:
            await create_expedient(worker_id, expedient, session)

        response = await token_handler.sign(worker_id, schema.email)
        return response
    except AlreadyExistsError as error:
        raise HTTPException(409, str(error))


@register_router.post('/validate')
async def validate_credentials(
        schema: ValidateCredentialsSchema,
        session: Annotated[AsyncSession, Depends(get_db_session)]
) -> list[ValidateFieldSchema]:
    availability = await check_availability(
        email=schema.email,
        doc_num=schema.doc_num,
        phone=schema.phone,
        session=session
    )
    fields_availability = zip(['email', 'doc_num', 'phone'], availability)

    create_validate_field_schema: Callable[[tuple[str, bool]], ValidateFieldSchema] = (
        lambda field_info: ValidateFieldSchema(
            field=field_info[0],
            available=field_info[1]
        )
    )

    return list(map(create_validate_field_schema, fields_availability))
