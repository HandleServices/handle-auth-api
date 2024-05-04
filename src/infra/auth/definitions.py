from src.utils import get_env_var

SECRET = get_env_var('JWT_SECRET')
ALGORITHM = get_env_var('JWT_ALGORITHM')
EXPIRY_TIME = 7200
