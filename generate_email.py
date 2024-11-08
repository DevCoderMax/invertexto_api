from bs4 import BeautifulSoup
import requests 

def generate_email():
    page = requests.get("https://www.invertexto.com/gerador-email-temporario").content
    soup = BeautifulSoup(page, 'html.parser') 
    email = soup.find(id='email-input') # pega o e-mail pelo elemento id
    return email.get('value') # retorna o e-mail

generate_email()