from typing import AsyncGenerator

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped

from src.db import async_session


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except SQLAlchemyError as error:
            session.rollback()
            raise Exception(error)


async def verify_existence[T, U](
        session: AsyncSession,
        model: T,
        column: Mapped[U],
        value: U
) -> bool:
    query = select(model).where(column == value)
    result = await session.scalar(query)
    return result is not None
