from src.utils import get_env_var

SECRET = get_env_var('JWT_SECRET')
JWT_ALGORYTHM = get_env_var('JWT_ALGORITHM')
EXPIRY_TIME = 7200
PASSWORD_ENCRYPTION_ALGORYTHM = 'SHA256'
