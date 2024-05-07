from typing import Annotated

from pydantic import StringConstraints

NameStr = Annotated[str, StringConstraints(
    strip_whitespace=True,
    max_length=50,
    min_length=2,
    pattern=r'^[A-Za-zÀ-ú]+'
)]

BusinessNameStr = Annotated[str, StringConstraints(
    max_length=50
)]

PhoneStr = Annotated[str, StringConstraints(
    min_length=10,
    max_length=15,
    pattern=r'^[\d]{11,15}$'
)]

DocumentStr = Annotated[str, StringConstraints(
    min_length=11,
    max_length=14,
    pattern=r'^(\d{11}|\d{14})$'
)]

