from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker

from src.utils import get_env_var

SYNC_DB_DRIVER = 'postgresql+psycopg2'

SYNC_DATABASE_URL = URL.create(
    drivername=SYNC_DB_DRIVER,
    username=get_env_var('DB_USER'),
    database=get_env_var('DB_NAME'),
    password=get_env_var('DB_PASSWORD'),
    host=get_env_var('DB_HOST'),
    port=int(get_env_var('DB_PORT'))
)

engine = create_engine(SYNC_DATABASE_URL)
LocalSession = sessionmaker(engine)
