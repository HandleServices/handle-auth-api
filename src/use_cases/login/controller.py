from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.utils import get_db_session
from src.infra.auth import AuthResponse, token_handler
from src.infra.exceptions import NotFoundError
from src.use_cases.login import repository
from src.use_cases.login.models import LoginSchema

login_router = APIRouter(tags=['Login'])


@login_router.post('')
async def login(
        schema: LoginSchema,
        session: Annotated[AsyncSession, Depends(get_db_session)]
) -> AuthResponse:
    try:
        authorized = await repository.check_credentials(schema.email, schema.password, session)

        if authorized is None:
            raise HTTPException(401, 'unauthorized')

        response = await token_handler.sign(uuid=authorized.worker_id, email=schema.email)
        return response

    except NotFoundError:
        raise HTTPException(404, 'user not found')
