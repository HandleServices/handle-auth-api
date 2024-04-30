from uuid import UUID as _UUID

from sqlalchemy import ForeignKey, UUID, Enum
from sqlalchemy.orm import Mapped, mapped_column

from src.common.enums import *
from src.db.definitions import Base


class Worker(Base):
    __tablename__ = 'workers'

    id: Mapped[_UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    gender: Mapped[str] = mapped_column(Enum(Gender, name='genders'))
    business_name: Mapped[str]
    job_id: Mapped[int] = mapped_column(ForeignKey('jobs.id'))
    email: Mapped[str] = mapped_column(unique=True)
    phone: Mapped[str] = mapped_column(unique=True)
    doc_num: Mapped[str] = mapped_column(Enum(DocType, name='doc_types'), unique=True)
    doc_type: Mapped[str] = mapped_column(Enum(DocType))
    profile_pic_url: Mapped[str]
