from src.modules.proxy_manager import ProxyManager
from src.modules.get_info import GetInfo
from src.modules.export_data import ExportData

from src.utils.shared.shared import shared_show_message_with_clear
from src.utils.system_utils import execute_before, create_file, extract_emails, delete_files_temp
from src.utils.style_outputs import (
    print_proxy_online, print_select_scraping_mode, print_invalid_value,
    print_proxy_disconnected, print_interrupted_message, print_error_unexpected,
    loading_animation, print_exit_message
)

from config.dorks_config import dorks_instagram, dorks_linkedin, dorks_tiktok
from config.colors_config import GREEN, RESET

from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from random import randint
from time import sleep
import threading
import sys

class MineScraper:
    def __init__(self, localhost: bool) -> None:
        self.chosen_city: str = None
        self.chosen_proxy: str = None
        self.driver: webdriver = None

        self._initialize_driver(localhost)

        self.standard_search: str = 'https://duckduckgo.com/'
        self.element_search_bar_xpath: str = '//*[@id="searchbox_input"]'
        self.element_more_results_button_xpath: str = '//*[@id="more-results"]'

        self.choice_scraping_mode: str = None

        self.search_content: str = None

        self.name_export: str = None

        self.socialmedia_platform: str = None

        self.dorks: list = []

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
                self.dorks = ['dork_instagram_gmail', 
                                'dork_instagram_outlook', 
                                'dork_instagram_yahoo', 
                                'dork_instagram_icloud', 
                                'dork_instagram_protonmail', 
                                'dork_instagram_aol', 
                                'dork_instagram_yandex',
                                'dork_instagram_mail',
                                'dork_instagram_gmx']
                
                shared_show_message_with_clear(lambda: print_proxy_online(self.chosen_city, self.chosen_proxy))

            case 2:
                self.dorks = ['dorks_linkedin_gmail',
                                'dorks_linkedin_outlook',
                                'dorks_linkedin_yahoo',
                                'dorks_linkedin_icloud',
                                'dorks_linkedin_protonmail',
                                'dorks_linkedin_aol',
                                'dorks_linkedin_yandex',
                                'dorks_linkedin_mail',
                                'dorks_linkedin_gmx']
                
                shared_show_message_with_clear(lambda: print_proxy_online(self.chosen_city, self.chosen_proxy))

            case 3:
                self.dorks = ['dorks_tiktok_gmail', 
                                'dorks_tiktok_outlook', 
                                'dorks_tiktok_yahoo', 
                                'dorks_tiktok_icloud', 
                                'dorks_tiktok_protonmail', 
                                'dorks_tiktok_aol', 
                                'dorks_tiktok_yandex',
                                'dorks_tiktok_mail',
                                'dorks_tiktok_gmx']
                                
                shared_show_message_with_clear(lambda: print_proxy_online(self.chosen_city, self.chosen_proxy))
            
            case 0:
                shared_show_message_with_clear(lambda: print_proxy_disconnected(self.chosen_city, self.chosen_proxy), print_exit_message)
                sys.exit(0)

            case _:
                shared_show_message_with_clear(lambda: print_proxy_online(self.chosen_city, self.chosen_proxy), lambda: print_invalid_value(self.choice_scraping_mode))
                self.pull_scraping_mode()
        
    def get_data(self) -> None:
        self.driver.get(self.standard_search)

        return

    def search_element(self, element: str, dork: str) -> None:
        search_bar = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, element)))
        search_bar.send_keys(dork)
        search_bar.send_keys(Keys.ENTER)
        
        return
    
    def click_until_disappear(self) -> None:
        while True:
            try:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.element_more_results_button_xpath))).click()
                sleep(randint(1, 3))
                
            except (TimeoutException, ElementClickInterceptedException):
                break

        return
            
    def save_all_search_content_temp(self, filename: str) -> None:
        self.search_content = self.driver.execute_script("return document.body.innerText;")

        create_file(filename, self.search_content)
        
        return
    
    def data_scraping(self, dork_name: str) -> None:
        match self.choice_scraping_mode:
            case 1:
                dork_query = dorks_instagram[dork_name]
                self.name_export = 'emails_data_instagram'
                self.socialmedia_platform = 'instagram'

            case 2:
                dork_query = dorks_linkedin[dork_name]
                self.name_export = 'emails_data_linkedin'
                self.socialmedia_platform = 'linkedin'

            case 3:
                dork_query = dorks_tiktok[dork_name]
                self.name_export = 'emails_data_tiktok'
                self.socialmedia_platform = 'tiktok'

        self.get_data()
        self.search_element(self.element_search_bar_xpath, dork_query)
        self.click_until_disappear()
        self.save_all_search_content_temp(dork_name)

        return

    def data_building(self, dork_name: str) -> None:
        emails = extract_emails(dork_name)
        create_file(dork_name, "\n".join(emails))
        
        return
    
    def execute(self) -> None:
            stop_event = threading.Event()
            loading_thread = None
            
            try:
                self.pull_scraping_mode()

                loading_thread = threading.Thread(target=loading_animation, args=("Scraping and Building data", stop_event))
                loading_thread.start()
                
                for dork_name in self.dorks:
                    self.data_scraping(dork_name)
                    self.data_building(dork_name)

                ExportData().export_to_excel(self.name_export, self.socialmedia_platform)

                shared_show_message_with_clear(lambda: print_proxy_online(self.chosen_city, self.chosen_proxy))
            
            except KeyboardInterrupt:
                shared_show_message_with_clear(lambda: print_proxy_disconnected(self.chosen_city, self.chosen_proxy), print_interrupted_message)
                self.driver.quit()
                sys.exit(1)

            except Exception:
                shared_show_message_with_clear(lambda: print_proxy_disconnected(self.chosen_city, self.chosen_proxy), print_error_unexpected)
                self.driver.quit()
                sys.exit(1)
            
            finally:
                if loading_thread is not None:
                    stop_event.set()
                    loading_thread.join()
                
                delete_files_temp()
                self.driver.quit()