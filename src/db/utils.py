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
    """
    Verifies if a record exists in the database table based on the given criteria.

    :param session: An asynchronous session object used for executing queries.
    :param model: The SQLAlchemy model representing the database table.
    :param column: The column of the model to query against.
    :param value: The value to match against the column.

    :return: True if a record exists with the provided value in the specified column, False otherwise.
    """
    query = select(model).where(column == value)
    result = await session.scalar(query)
    return result is not None
