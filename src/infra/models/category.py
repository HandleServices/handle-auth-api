from sqlalchemy.orm import Mapped, mapped_column

from src.db.definitions import Base


class Category(Base):
    __tablename__ = 'job_categories'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
