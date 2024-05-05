from fastapi import FastAPI

from src.use_cases.login.controller import login_router

app = FastAPI()
app.include_router(login_router, prefix='/login')
