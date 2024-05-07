from typing import Literal

from pydantic import EmailStr, BaseModel

from src.use_cases.register.models.types import PhoneStr, DocumentStr


class ValidateCredentialsSchema(BaseModel):
    email: EmailStr
    doc_num: DocumentStr
    phone: PhoneStr


class ValidateFieldSchema(BaseModel):
    field: Literal['email', 'doc_num', 'phone']
    available: bool
