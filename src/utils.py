import os


def get_env_var(var_name: str) -> str:
    if env_var := os.environ.get(var_name):
        return env_var

    raise Exception(f'Missing environment variable: {var_name}')
