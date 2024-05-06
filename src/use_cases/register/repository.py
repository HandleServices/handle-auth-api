from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from src.db.utils import verify_existence
from src.infra.auth.crypto import encrypt_password
from src.infra.exceptions import AlreadyExistsError
from src.infra.models import Worker, WorkerLogin, Expedient
from src.use_cases.register.models import RegisterSchema, ExpedientSchema


# todo create functions that validates every field of worker

async def check_availability(email: str, doc: str, phone: str, session: AsyncSession):
    if await verify_existence(session, Worker, Worker.email, email):
        raise AlreadyExistsError('An account with the provided email already exists')
    if await verify_existence(session, Worker, Worker.doc_num, doc):
        raise AlreadyExistsError('An account with the provided document already exists')
    if await verify_existence(session, Worker, Worker.phone, phone):
        raise AlreadyExistsError('An account with the provided phone already exists')


async def create_worker(data: RegisterSchema, session: AsyncSession) -> UUID:
    await check_availability(data.email, data.doc_num, data.phone, session)
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
