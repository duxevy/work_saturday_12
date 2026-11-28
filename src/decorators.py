from typing import Callable, Any
from functools import wraps
import os

path_to_log = "logs/foo3_log.txt"

def log_to_file(path: str = path_to_log) -> Callable:
    def decorator(func) -> Callable:
        """Это декоратор"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Это обёртка"""
            try:
                os.mkdir("logs")
            except FileExistsError:
                pass
            with open(path, "w", encoding="utf-8") as f:
                f.write(f"[{func.__name__}] Начало работы функции. Аргументы: {args}, {kwargs}\n")
                result = func(*args, **kwargs)
                f.write(f"[{func.__name__}] Конец работы функции. Результат: {result}\n")
            return result
        return wrapper
    return decorator

@log_to_file()
def foo(a, b):
    return a + b

foo(1, 2)