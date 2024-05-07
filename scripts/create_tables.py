from dotenv import load_dotenv

load_dotenv()
from scripts.common import engine

from src.db.definitions import Base

if __name__ == '__main__':
    Base.metadata.create_all(engine)
