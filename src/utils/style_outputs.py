from config.colors_config import WHITE, YELLOW, ORANGE, RED, GREEN, RESET, BOLD

from itertools import cycle
from time import sleep
import threading
import sys

def print_welcome_message() -> None:
    print(rf'''{GREEN}{BOLD}
8b   d8 w                .d88b.                               
8YbmdP8 w 8d8b. .d88b    YPwww. .d8b 8d8b .d88 88b. .d88b 8d8b
8  "  8 8 8P Y8 8.dP'        d8 8    8P   8  8 8  8 8.dP' 8P  
8     8 8 8   8 `Y88P    `Y88P' `Y8P 8    `Y88 88P' `Y88P 8   
                                               8             

        {RESET}{WHITE}Web {GREEN}Scraping{WHITE} for data extraction and processing 
            {RESET}{GREEN}
    [*]__author__: {RESET}George Victor | @id0ubl3g{GREEN}
    [*]__github__: {RESET}github.com/id0ubl3g/mine-scraper{GREEN}
    [*]__usage__: {YELLOW}python3{RESET} run.py --localhost {GREEN}<True/False>{RESET}{WHITE} | Configure proxy behavior{RESET}''')

def print_select_scraping_mode() -> None:
    print(f'\n{GREEN}[+]{RESET}{BOLD} Select a scraping mode:{RESET}\n')
    print(f'{GREEN}[1]{RESET} Instagram: Scrape emails from pages')
    print(f'{GREEN}[2]{RESET} Linkedin: Scrape emails from pages')
    print(f'{GREEN}[3]{RESET} TikTok: Scrape emails from pages')
    print(f'{GREEN}[0]{RESET} Exit: Exit the scraper')

def print_exit_message() -> None:
    print(f'\n{ORANGE}[!]{RESET} Exiting gracefully. Thank you for using the Mine Scraper!')
    sleep(0.5)
    
def print_interrupted_message() -> None:
    print(f'\n{ORANGE}[!]{RESET} Operation interrupted by user. Exiting gracefully...')

def print_invalid_value(message: str) -> None:
    print(f'\n{ORANGE}[i]{RESET} Invalid value: {WHITE}{message}{RESET}')

def print_error_unexpected() -> None:
    print(f'\n{RED}[x]{RESET} An unexpected error occurred.')

def print_error_choosing_proxy() -> None:
    print(f'\n{RED}[x]{RESET} An error occurred while choosing the proxy.')

def print_error_connect_proxy(chosen_city) -> None:
    print(f'{RED}[x]{RESET} An error occurred while connect to the proxy: {chosen_city}')

def print_error_testing_proxy(chosen_city) -> None:
    print(f'\n{RED}[x]{RESET} An error occurred while testing the proxy: {chosen_city}')

def print_proxy_online(chosen_city, chosen_proxy) -> None:
    print(f'\n{GREEN}•{RESET}{WHITE} Proxy: {chosen_city} | {chosen_proxy} (Online){RESET}')

def print_proxy_disconnected(chosen_city, chosen_proxy) -> None:
    print(f'\n{RED}•{RESET}{WHITE} Proxy: {chosen_city} | {chosen_proxy} (Disconnected){RESET}')

def loading_animation(message: str, stop_event: threading.Event) -> None:
    spinner = cycle(["|", "/", "-", "\\"])
    
    sys.stdout.write("\n")
    while not stop_event.is_set():
        sys.stdout.write(f"\r{GREEN}[→]{RESET} {message} {next(spinner)}")
        sys.stdout.flush()
        sleep(0.1)
    
    sys.stdout.write("\r" + " " * (len(message) + 10) + "\r")
    sys.stdout.flush()