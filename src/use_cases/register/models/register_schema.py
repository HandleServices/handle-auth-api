from pydantic import BaseModel, EmailStr

from src.infra.enums import Gender, DocType
from src.use_cases.register.models.expedient_schema import ExpedientSchema


class RegisterSchema(BaseModel):
    password: str
    email: EmailStr
    first_name: str
    last_name: str
    gender: Gender
    business_name: str
    job_id: int
    phone: str
    doc_num: str
    doc_type: DocType
    expedient: list[ExpedientSchema]
