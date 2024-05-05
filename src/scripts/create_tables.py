from dotenv import load_dotenv

load_dotenv()
from src.scripts.common import engine

from src.db.definitions import Base
from src.infra.models import *

if __name__ == '__main__':
    Base.metadata.create_all(engine)
