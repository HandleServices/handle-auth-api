from typing import ClassVar

from pydantic import BaseModel
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm.decl_api import DeclarativeAttributeIntercept

from src.infra.pydantic import to_pydantic
from src.utils import get_env_var

DATABASE_URL = URL.create(
    drivername=get_env_var('DB_DRIVER'),
    username=get_env_var('DB_USER'),
    database=get_env_var('DB_NAME'),
    password=get_env_var('DB_PASSWORD'),
    host=get_env_var('DB_HOST'),
    port=int(get_env_var('DB_PORT'))
)

engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(engine)


class BaseMeta(DeclarativeAttributeIntercept):
    @property
    def pydantic(cls):
        return to_pydantic(cls)


class Base(DeclarativeBase, metaclass=BaseMeta):
    pydantic: ClassVar[BaseModel]
