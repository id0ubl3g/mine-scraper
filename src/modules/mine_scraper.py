from src.modules.proxy_manager import ProxyManager
from src.modules.get_info import GetInfo

from src.utils.shared.shared import shared_show_message_with_clear
from src.utils.system_utils import execute_before
from src.utils.style_outputs import (
    print_proxy_online, print_select_scraping_mode, print_invalid_value,
    print_proxy_disconnected, print_interrupted_message, print_error_unexpected
)

from config.dorks_config import dorks_instagram
from config.colors_config import GREEN, RESET

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import sys

class MineScraper:
    def __init__(self, localhost: bool) -> None:
        self.chosen_city: str = None
        self.chosen_proxy: str = None
        self.driver: webdriver = None

        self._initialize_driver(localhost)

        self.standard_search: str = 'https://duckduckgo.com/'
        self.element_search_bar_xpath: str = '//*[@id="searchbox_input"]'

        self.choice_scraping_mode: str = None

        self.dork_one: str = None
        self.dork__two: str = None

    def _initialize_driver(self, localhost: bool) -> None:
        if not localhost:
            self.chosen_city, self.chosen_proxy = ProxyManager().test_proxy()
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(f'--proxy-server={self.chosen_proxy}')
            self.driver = webdriver.Chrome(options=chrome_options)
        
        else:
            self.chosen_city, self.chosen_proxy = GetInfo().get_ip_and_country()
            self.driver = webdriver.Chrome()

    def select_scraping_mode(self) -> None:
        while True:
            try:
                shared_show_message_with_clear(lambda: print_proxy_online(self.chosen_city, self.chosen_proxy), print_select_scraping_mode, delay=0.0)
                self.choice_scraping_mode = input(F'{GREEN}\n[$] {RESET}')

                if self.choice_scraping_mode.strip():
                    self.choice_scraping_mode = int(self.choice_scraping_mode)

                    return
                
                else:
                    shared_show_message_with_clear(lambda: print_proxy_online(self.chosen_city, self.chosen_proxy), lambda: print_invalid_value(self.choice_scraping_mode))

            except ValueError:
                shared_show_message_with_clear(lambda: print_proxy_online(self.chosen_city, self.chosen_proxy), lambda: print_invalid_value(self.choice_scraping_mode))


    @execute_before(select_scraping_mode)
    def pull_scraping_mode(self) -> None:
        match self.choice_scraping_mode:
            case 1:
                self.dork_one = dorks_instagram['dork_instagram_one']
                self.dork_two = dorks_instagram['dork_instagram_two']
            
            case _:
                shared_show_message_with_clear(lambda: print_proxy_online(self.chosen_city, self.chosen_proxy), lambda: print_invalid_value(self.choice_scraping_mode))
                self.pull_scraping_mode()
        
    def get_data(self) -> None:
        self.driver.get(self.standard_search)      
    
        return

    def send_keys(self, element: str, dork: str) -> None:
        search_bar = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, element)))
        search_bar.send_keys(dork)
        search_bar.send_keys(Keys.ENTER)
        
        return

    def execute(self) -> None:
            try:
                self.pull_scraping_mode()
                self.get_data()
                self.send_keys(self.element_search_bar_xpath, self.dork_one)
                
                sleep(50)
                
                self.driver.quit()
            
            except KeyboardInterrupt:
                shared_show_message_with_clear(lambda: print_proxy_disconnected(self.chosen_city, self.chosen_proxy), print_interrupted_message)
                sys.exit(1)

            except Exception:
                shared_show_message_with_clear(lambda: print_proxy_disconnected(self.chosen_city, self.chosen_proxy), print_error_unexpected)
                sys.exit(1)