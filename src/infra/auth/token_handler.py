from time import time
from typing import Optional
from uuid import UUID

import jwt

from src.infra.auth.auth_response import AuthResponse
from src.infra.auth.definitions import ALGORITHM, EXPIRY_TIME, SECRET

type json = dict[str, any]


def sign(uuid: UUID, email: str) -> AuthResponse:
    payload = {
        'user_id': str(uuid),
        'user_email': email,
        'exp': time() + EXPIRY_TIME
    }
    token = jwt.encode(payload=payload, key=SECRET, algorithm=ALGORITHM)
    return AuthResponse(access_token=token)


def decode(token: str) -> Optional[json]:
    try:
        decode_token: json = jwt.decode(
            jwt=token, key=SECRET, algorithms=[ALGORITHM]
        )
        if decode_token['exp'] >= time():
            return decode_token
    except jwt.DecodeError as e:
        print(e)
    return None
