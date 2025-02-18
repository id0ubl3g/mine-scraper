from src.utils.shared.shared import shared_show_message_with_clear

from docs.usage_mine_scraper import usage_mine_scraper

from typing import Callable
import argparse
import sys
import os
import re

def clear_screen() -> None:
    os.system('clear')

def create_file(filename: str, search_content: str) -> None:
    os.makedirs('src/temp', exist_ok=True)
    file_path = os.path.join('src/temp', f"{filename}.txt")
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(search_content)
    
def extract_emails(filename) -> list:
    os.makedirs('src/temp', exist_ok=True)
    file_path = os.path.join('src/temp', f"{filename}.txt")

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    email_pattern = r'\b[A-Za-z0-9][A-Za-z0-9._%+-]{0,63}@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    emails = re.findall(email_pattern, content)
    
    invalid_suffixes = ('.Watch', '.Xem', '.Schau', '.Mira')
    cleaned_emails = [email.rsplit('.', 1)[0] if email.endswith(invalid_suffixes) else email for email in emails]


    unique_emails = sorted(set(cleaned_emails))

    return unique_emails

def delete_files_temp() -> None:
    for file in os.listdir('src/temp'):
        file_path = os.path.join('src/temp', file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    return

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