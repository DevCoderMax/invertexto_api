import requests
from bs4 import BeautifulSoup
from typing import Dict, Any

class IP:
    def __init__(self, ip: str):
        self._ip = ip
        self._base_url = "https://www.invertexto.com"
        self._api_url = "https://api.invertexto.com/v1/geoip"
    
    @staticmethod
    def my_ip() -> str:
        try:
            response = requests.get("https://www.invertexto.com/meu-ip")
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.find('span', class_='meu-ip').text.strip()
        except Exception as e:
            raise Exception(f"Erro ao obter IP: {str(e)}")
    
    def LocalIP(self) -> Dict[str, Any]:
        try:
            # Obtém o token
            response = requests.get(f"{self._base_url}/localizar-ip")
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            script = soup.find('script', string=lambda t: t and 'token=' in t)
            if not script:
                raise ValueError("Token não encontrado")
                
            token = script.string.split('token=')[1].split("'")[0]
            
            # Faz a requisição da API
            response = requests.get(
                f"{self._api_url}/{self._ip}",
                params={"token": token}
            )
            response.raise_for_status()
            
            return response.json()
        except Exception as e:
            raise Exception(f"Erro ao obter informações do IP: {str(e)}")
