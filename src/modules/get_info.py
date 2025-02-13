import requests

class GetInfo:
    def __init__(self) -> None:
        self.site: str = 'http://ip-api.com/json'

    def get_ip_and_country(self) -> tuple[str, str]:
        response = requests.get(self.site)
        
        if response.status_code == 200:
            data = response.json()
            
            country = data.get("country", "Not found")
            ip = data.get("query", "Localhost")
            
            return country, f'{ip} - Localhost'

        return 'Not found', 'Localhost'