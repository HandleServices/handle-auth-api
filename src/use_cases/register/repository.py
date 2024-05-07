from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from src.db.utils import verify_existence
from src.infra.auth.crypto import encrypt_password
from src.infra.exceptions import AlreadyExistsError
from src.infra.models import Worker, WorkerLogin, Expedient
from src.use_cases.register.models import RegisterSchema, ExpedientSchema


async def ensure_unique_worker_credentials(email: str, doc: str, phone: str, session: AsyncSession):
    """
    Checks the availability of email, document number (doc), and phone number in the workers table
    to ensure uniqueness.
    If any of the parameters already exists raises an AlreadyExistsError

    :param email: The email address to ensure uniqueness.
    :param doc: The document number to ensure uniqueness
    :param phone The phone number to ensure uniqueness
    :param session: An AsyncSession instance to execute asynchronous database queries.
    :raises: AlreadyExistsError if any of the provided email, doc and phone exists in workers table
    """
    if await verify_existence(session, Worker, Worker.email, email):
        raise AlreadyExistsError('An account with the provided email already exists')
    if await verify_existence(session, Worker, Worker.doc_num, doc):
        raise AlreadyExistsError('An account with the provided document already exists')
    if await verify_existence(session, Worker, Worker.phone, phone):
        raise AlreadyExistsError('An account with the provided phone already exists')


async def check_worker_credentials_availability(
        email: str,
        doc_num: str,
        phone: str,
        session: AsyncSession
) -> tuple[bool, bool, bool]:
    """
    Checks the availability of email, document number (doc), and phone number in the database.

    :param email: The email address to check for availability.
    :param doc_num: The document number to check for availability.
    :param phone: The phone number to check for availability.
    :param session: An AsyncSession instance to execute asynchronous database queries.

    :return: A tuple containing Boolean values indicating the availability of email, doc, and phone respectively.
             Each element in the tuple represents whether the corresponding data is available (True) or not (False).
    """

    email_available = not await verify_existence(session, Worker, Worker.email, email)
    doc_available = not await verify_existence(session, Worker, Worker.doc_num, doc_num)
    phone_available = not await verify_existence(session, Worker, Worker.phone, phone)
    return email_available, doc_available, phone_available


async def create_worker(data: RegisterSchema, session: AsyncSession) -> UUID:
    await ensure_unique_worker_credentials(data.email, data.doc_num, data.phone, session)
    worker = Worker(
        first_name=data.first_name,
        last_name=data.last_name,
        gender=data.gender,
        business_name=data.business_name,
        job_id=data.job_id,
        email=data.email,
        phone=data.phone,
        doc_num=data.doc_num,
        doc_type=data.doc_type,
        profile_pic_url=None
    )
    session.add(worker)
    await session.flush()
    return worker.id


async def create_expedient(worker_id: UUID, data: ExpedientSchema, session: AsyncSession):
    expedient = Expedient(
        worker_id=worker_id,
        week_day=data.week_day,
        start_time=data.start_time,
        end_time=data.end_time
    )
    session.add(expedient)


async def create_worker_login(worker_id: UUID, password: str, session: AsyncSession):
    encrypted_password, salt = encrypt_password(password)
    worker_login = WorkerLogin(
        worker_id=worker_id,
        hashed_password=encrypted_password,
        salt=salt
    )
    session.add(worker_login)
