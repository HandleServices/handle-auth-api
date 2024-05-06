from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.utils import get_db_session
from src.infra.auth import AuthResponse, token_handler
from src.infra.exceptions import AlreadyExistsError
from src.use_cases.register import repository
from src.use_cases.register.models import RegisterSchema
from src.use_cases.register.repository import create_expedient

register_router = APIRouter()


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
