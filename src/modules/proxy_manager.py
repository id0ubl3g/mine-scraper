from src.utils.shared.shared import shared_show_message_with_clear
from src.utils.system_utils import execute_before
from src.utils.style_outputs import ( 
    print_interrupted_message, print_error_choosing_proxy, print_proxy_disconcerted,
    print_error_connect_proxy, print_error_testing_proxy
)

from config.proxies_config import *

from random import randint
import requests
import sys

class ProxyManager():
    def __init__(self):
        self.cities: list['str'] = []
        self.quantity_proxies: int = None
        self.random_number: int = None
        
        self.chosen_city: str = None
        self.chosen_proxy: str = None

        self.use_protocol: str = 'http'

    def choosing_proxy(self) -> None:
        try:
            for country, _ in proxies_http.items():
                self.cities.append(country)

            self.quantity_proxies = len(proxies_http)
            self.random_number = randint(0, self.quantity_proxies - 1)

            self.chosen_city = self.cities[self.random_number]
            self.chosen_proxy = proxies_http[self.chosen_city]
        
        except KeyboardInterrupt:
            shared_show_message_with_clear(print_interrupted_message)
            sys.exit(1)

        except Exception:
            shared_show_message_with_clear(print_error_choosing_proxy)
            sys.exit(1)
    
    @execute_before(choosing_proxy)
    def test_proxy(self) -> tuple['str', 'str']:
        proxies = {self.use_protocol: self.chosen_proxy}
        try:
            response = requests.get("https://www.duckduckgo.com", proxies=proxies, timeout=30)
            if response.status_code == 200:
                
                return self.chosen_city, self.chosen_proxy
            
            shared_show_message_with_clear(lambda: print_proxy_disconcerted(self.chosen_city, self.chosen_proxy), print_error_connect_proxy(self.chosen_city))
            sys.exit(1)

        except KeyboardInterrupt:
                shared_show_message_with_clear(lambda: print_proxy_disconcerted(self.chosen_city, self.chosen_proxy), print_interrupted_message)
                print_proxy_disconcerted(self.chosen_city, self.chosen_proxy)
                sys.exit(1)

        except Exception:
            shared_show_message_with_clear(lambda: print_proxy_disconcerted(self.chosen_city, self.chosen_proxy), print_error_testing_proxy(self.chosen_city))
            sys.exit(1)