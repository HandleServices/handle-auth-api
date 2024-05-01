from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db.definitions import Base


class Job(Base):
    __tablename__ = 'jobs'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category_id: Mapped[int] = mapped_column(ForeignKey('job_categories.id'))
    name: Mapped[str]
