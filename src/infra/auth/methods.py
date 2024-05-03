from time import time
from uuid import UUID, uuid4

import jwt

from src.infra.auth.auth_response import AuthResponse
from src.infra.auth.definitions import ALGORITHM, EXPIRY_TIME, SECRET


def sign(uuid: UUID, email: str) -> AuthResponse:
    payload = {
        'user_id': str(uuid),
        'user_email': email,
        'expiry': time() + EXPIRY_TIME
    }
    token = jwt.encode(payload=payload, key=SECRET, algorithm=ALGORITHM)
    return AuthResponse(access_token=token)


def decode(token: str) -> dict[str, any] | None:
    try:
        decode_token: dict[str, any] = jwt.decode(
            jwt=token, key=SECRET, algorithms=[ALGORITHM]
        )
        if decode_token["expiry"] >= time():
            return decode_token
    except jwt.DecodeError as e:
        print(e)
    return None