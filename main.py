import uvicorn
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()

    uvicorn.run(app='src.app:app', host='localhost', port=9000)
