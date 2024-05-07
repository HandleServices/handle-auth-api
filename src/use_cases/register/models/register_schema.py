from pydantic import BaseModel, EmailStr

from src.infra.enums import Gender, DocType
from src.use_cases.register.models.expedient_schema import ExpedientSchema
from src.use_cases.register.models.types import NameStr, BusinessNameStr, PhoneStr, DocumentStr


class RegisterSchema(BaseModel):
    password: str
    email: EmailStr
    first_name: NameStr
    last_name: NameStr
    gender: Gender
    business_name: BusinessNameStr
    job_id: int
    phone: PhoneStr
    doc_num: DocumentStr
    doc_type: DocType
    expedient: list[ExpedientSchema]
