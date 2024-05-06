from fastapi import FastAPI

from src.use_cases.login.controller import login_router
from src.use_cases.register.controller import register_router

app = FastAPI()


app.include_router(login_router, prefix='/login')
app.include_router(register_router, prefix='/register')
