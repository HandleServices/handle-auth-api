from dotenv import load_dotenv

load_dotenv()

from src.db.definitions import Base
from src.infra.models import *


from sqlalchemy import URL, create_engine

from src.utils import get_env_var

SYNC_DB_DRIVER = 'postgresql+psycopg2'

DATABASE_URL = URL.create(
    drivername=SYNC_DB_DRIVER,
    username=get_env_var('DB_USER'),
    database=get_env_var('DB_NAME'),
    password=get_env_var('DB_PASSWORD'),
    host=get_env_var('DB_HOST'),
    port=int(get_env_var('DB_PORT'))
)

if __name__ == '__main__':
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
