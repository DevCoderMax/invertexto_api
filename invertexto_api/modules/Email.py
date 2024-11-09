import requests
from bs4 import BeautifulSoup
from typing import Dict, Any

class Email:
    def __init__(self):
        self._base_url = "https://www.invertexto.com/gerador-email-temporario?email="
        self._end_url = "@uorak.com"

    def generate_email():
        page = requests.get("https://www.invertexto.com/gerador-email-temporario").content
        soup = BeautifulSoup(page, 'html.parser') 
        email = soup.find(id='email-input') # pega o e-mail pelo elemento id
        return email.get('value') # retorna o e-mail

    generate_email()