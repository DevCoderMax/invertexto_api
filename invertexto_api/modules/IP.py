import requests
from bs4 import BeautifulSoup

class ip:
    def __init__(self, ip: str):
        self.ip = ip
    
    def my_ip():
        url = "https://www.invertexto.com/meu-ip"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        ip = soup.find('span', class_='meu-ip').text
        return ip
    
    def LocalIP(self):

        # capturando token

        url_token = "https://www.invertexto.com/localizar-ip"

        # capturando token
        response = requests.get(url_token)

        soup = BeautifulSoup(response.text, 'html.parser')
        token = soup.find('script', string=lambda t: t and 'token=' in t).string.split('token=')[1].split("'")[0]

        # buscando ip indicado

        url_api = "https://api.invertexto.com/v1/geoip/"
        ip = self.ip
        token_url = "?token="
        
        full_url = url_api+ip+token_url+token

        response = requests.get(full_url)

        return response.json()
    

