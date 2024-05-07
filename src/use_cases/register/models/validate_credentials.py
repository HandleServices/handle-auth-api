from typing import Literal, Optional

from pydantic import EmailStr, BaseModel

from src.use_cases.register.models.types import PhoneStr, DocumentStr


class ValidateCredentialsSchema(BaseModel):
    email: Optional[EmailStr]
    doc_num: Optional[DocumentStr]
    phone: Optional[PhoneStr]


class ValidateFieldSchema(BaseModel):
    field: Literal['email', 'doc_num', 'phone']
    available: bool
