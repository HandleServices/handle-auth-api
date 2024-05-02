from typing import ClassVar

from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm.decl_api import DeclarativeAttributeIntercept

from src.infra.pydantic import to_pydantic


class BaseMeta(DeclarativeAttributeIntercept):
    @property
    def pydantic(cls):
        return to_pydantic(cls)


class Base(DeclarativeBase, metaclass=BaseMeta):
    pydantic: ClassVar[BaseModel]
