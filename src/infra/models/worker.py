from uuid import UUID as _UUID

from sqlalchemy import ForeignKey, UUID, Enum, text, String
from sqlalchemy.orm import Mapped, mapped_column

from src.infra.enums import *
from src.db.definitions import Base


class Worker(Base):
    __tablename__ = 'workers'

    id: Mapped[_UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text('gen_random_uuid()')
    )
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    gender: Mapped[Gender] = mapped_column(Enum(Gender, name='genders'))
    business_name: Mapped[str] = mapped_column(String(50))
    job_id: Mapped[int] = mapped_column(ForeignKey('jobs.id'))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    phone: Mapped[str] = mapped_column(String(15), unique=True)
    doc_num: Mapped[str] = mapped_column(String(14), unique=True)
    doc_type: Mapped[DocType] = mapped_column(Enum(DocType, name='doc_types'))
    profile_pic_url: Mapped[str | None]
