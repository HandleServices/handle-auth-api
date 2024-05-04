from uuid import UUID as _UUID

from sqlalchemy import ForeignKey, UUID, CHAR
from sqlalchemy.orm import Mapped, mapped_column

from src.db.definitions import Base


class WorkerLogin(Base):
    __tablename__ = 'workers_login'

    worker_id: Mapped[_UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey('workers.id'),
        primary_key=True
    )
    hash_password: Mapped[str] = mapped_column(CHAR(length=64))
    salt: Mapped[_UUID] = mapped_column(UUID(as_uuid=True))
