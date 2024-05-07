from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.auth.crypto import salt_then_encrypt_password
from src.infra.exceptions import NotFoundError
from src.infra.models import WorkerLogin, Worker


async def check_credentials(email: str, password: str, session: AsyncSession) -> WorkerLogin | None:
    """
    Checks if the provided email and password match any existing worker login credentials.

    :param email: The email associated with the worker.
    :param password: The password to be checked.
    :param session: An asynchronous session object used for executing queries.

    :return: If the credentials are valid, returns the corresponding WorkerLogin object.
             If the credentials are invalid, returns None.
    :raises NotFoundError: If no worker login information is found for the provided email.
    """
    query = (
        select(WorkerLogin)
        .join(Worker, Worker.id == WorkerLogin.worker_id)
        .where(Worker.email.__eq__(email))
    )
    login = await session.scalar(query)
    if login is None:
        raise NotFoundError()
    encrypted_password = salt_then_encrypt_password(password, str(login.salt))
    if encrypted_password != login.hashed_password:
        return None
    return login
