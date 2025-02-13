from src.utils.shared.shared import shared_show_message_with_clear

from docs.usage_mine_scraper import usage_mine_scraper

from typing import Callable
import argparse
import sys
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

def parse_arguments() -> bool:
    if '--help' in sys.argv or '-h' in sys.argv:
        clear_screen()
        print(usage_mine_scraper)
        sys.exit(0)
    
    parser = argparse.ArgumentParser(description='Set Localhost', usage='%(prog)s --localhost <True/False>')
    parser.add_argument(
        '-l', '--localhost', 
        type=str,
        help='Set Localhost | Use "True" or "False" for proxy',
        required=True
    )
    try:
        args = parser.parse_args()

        localhost_value = args.localhost.lower()

        if localhost_value == 'true':
            return True
        
        elif localhost_value == 'false':
            return False
        
        shared_show_message_with_clear(delay=0.0)
        sys.exit(1)

    except SystemExit:
        shared_show_message_with_clear(delay=0.0)
        sys.exit(1)