from datetime import time

from pydantic import BaseModel

from src.infra.enums import WeekDay


class ExpedientSchema(BaseModel):
    week_day: WeekDay
    start_time: time
    end_time: time
