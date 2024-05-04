import hashlib
from typing import Callable
from uuid import uuid4

from gloe import transformer, partial_transformer
from gloe.utils import forward_incoming, forget

type PasswordInfo = tuple[str, str]


@partial_transformer
def generate_salt(data: None, generator: Callable[[], str]) -> str:
    return generator()


@transformer
def salt_password(credentials: PasswordInfo) -> PasswordInfo:
    salt, password = credentials
    return f'{password}{salt}', salt


@partial_transformer
def encrypt_password_by_algorythm(credentials: PasswordInfo, algorythm: str) -> PasswordInfo:
    password, salt = credentials
    h = hashlib.new(algorythm, password.encode())
    return h.hexdigest(), salt


def encrypt_password(password: str) -> PasswordInfo:
    """
    Encrypts a given password with a randomly generated salt using SHA-256.

    This function performs three main steps:
    1. Generates a unique salt using UUID4.
    2. Salts the input password with the generated salt.
    3. Encrypts the salted password using SHA-256.

    :param password: The plaintext password to be encrypted.
    :type password: str

    :return: A tuple containing the encrypted password concatenated with the salt and the salt itself
    :rtype: tuple[str, str]
    """

    encrypt_password_sha256 = encrypt_password_by_algorythm('SHA256')

    generate_salt_uuid4 = generate_salt(lambda: str(uuid4()))

    encryption_pipeline = (
            forward_incoming(forget >> generate_salt_uuid4) >>
            salt_password >>
            encrypt_password_sha256
    )
    return encryption_pipeline(password)


def salt_then_encrypt_password(password: str, salt: str) -> PasswordInfo:
    """
    Encrypts a given password with the given salt using SHA-256.

    This function performs two main steps:
    1. Salts the input password with the given salt.
    2. Encrypts the salted password using SHA-256.

    :param password: The plaintext password to be encrypted.
    :type password: str

    :param salt: the salt that the password will be encrypted with
    :type salt: str

    :return: A tuple containing the encrypted password concatenated with the salt and the salt itself
    :rtype: tuple[str, str]
    """

    encrypt_password_sha256 = encrypt_password_by_algorythm('SHA256')

    encryption_pipeline = salt_password >> encrypt_password_sha256

    return encryption_pipeline((salt, password))
