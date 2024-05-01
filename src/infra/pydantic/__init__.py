from typing import TypeVar, get_args
from sqlalchemy.orm import DeclarativeBase
from pydantic import BaseModel, create_model

_B = TypeVar('_B', bound=DeclarativeBase)


def to_pydantic(base: type[_B]) -> type[BaseModel]:
    fields = {
        field: (get_args(mapped_type)[0], None)
        for field, mapped_type in base.__dict__['__annotations__'].items()
    }

    return create_model(base.__name__, **fields)
