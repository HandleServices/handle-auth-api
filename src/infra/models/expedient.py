from datetime import time
from uuid import UUID

from sqlalchemy import ForeignKey, Enum, TIME
from sqlalchemy.orm import Mapped, mapped_column

from src.infra.enums import WeekDay
from src.db.definitions import Base


class Expedient(Base):
    __tablename__ = 'expedients'

    worker_id: Mapped[UUID] = mapped_column(ForeignKey('workers.id'), primary_key=True)
    week_day: Mapped[WeekDay] = mapped_column(Enum(WeekDay, name='week_days'), primary_key=True)
    start_time: Mapped[time] = mapped_column(TIME(timezone=False))
    end_time: Mapped[time] = mapped_column(TIME(timezone=False))
