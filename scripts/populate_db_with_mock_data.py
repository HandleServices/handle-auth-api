from datetime import time
from uuid import UUID

from dotenv import load_dotenv

load_dotenv()
from src.infra.auth.crypto import salt_then_encrypt_password
from src.infra.enums import *
from src.infra.models import Job, Category, Worker, WorkerLogin, Expedient
from scripts.common import LocalSession

if __name__ == '__main__':
    with LocalSession() as session:
        generic_category = Category(name='generic')
        session.add(generic_category)
        session.commit()

        generic_job = Job(category_id=generic_category.id, name='generic_job')
        session.add(generic_job)
        session.commit()

        generic_worker = Worker(
            first_name='carlos',
            last_name='adalberto',
            gender=Gender.MALE,
            business_name='chaveiro arruda',
            job_id=generic_job.id,
            email='carlos@email.com',
            phone='11988776655',
            doc_num='11122233344',
            doc_type=DocType.CPF,
            profile_pic_url=None
        )
        session.add(generic_worker)
        session.commit()

        generic_expedient = Expedient(
            worker_id=generic_worker.id,
            week_day=WeekDay.MON,
            start_time=time(hour=8, minute=30),
            end_time=time(hour=18, minute=0)
        )
        session.add(generic_expedient)
        session.commit()

        generic_worker_password = 'teste'
        generic_worker_salt = '53f995c7-45eb-4bcf-bb94-a1ed84e5ba7d'
        generic_worker_credentials = salt_then_encrypt_password(
            generic_worker_password, generic_worker_salt
        )
        hashed_password = generic_worker_credentials

        generic_worker_login = WorkerLogin(
            worker_id=generic_worker.id,
            hashed_password=hashed_password,
            salt=UUID(hex=generic_worker_salt)
        )
        session.add(generic_worker_login)
        session.commit()
