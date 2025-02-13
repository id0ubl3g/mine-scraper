from src.utils.shared.shared import *

from typing import Callable
import os

def clear_screen() -> None:
    os.system('clear')

def execute_before(method_to_execute: Callable[[], None]) -> Callable[[], None]:
    def decorator(func: Callable[[], None]) -> Callable[[], None]:
        def wrapper(self, *args, **kwargs) -> None:
            method_to_execute(self)
            return func(self, *args, **kwargs)
        return wrapper
    return decorator