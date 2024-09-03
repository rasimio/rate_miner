from functools import wraps


def auth_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        print(f"auth {kwargs}")
        return await func(*args, **kwargs)
    return wrapper
