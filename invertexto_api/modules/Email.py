import json
import requests
from bs4 import BeautifulSoup
from typing import Dict, Any

class Email:
    def __init__(self):
        self._base_url = "https://www.invertexto.com/gerador-email-temporario?email="
        self._end_url = "@uorak.com"

    def generate_email(self):
        page = requests.get("https://www.invertexto.com/gerador-email-temporario").content
        soup = BeautifulSoup(page, 'html.parser')
        email = soup.find(id='email-input')
        return email.get('value')

    def create_custom_email(self, username: str):
        if not username:
            raise ValueError("O nome de usuário é obrigatório")

        end_url = self._base_url + username + self._end_url
        email = username + self._end_url

        response = requests.get(end_url)

        if email in response.text:
            return response.text
        else:
            raise ValueError("Email não encontrado")
        
    def list_emails(self, username: str) -> list[Dict[str, Any]]:
        if not username:
            raise ValueError("O nome de usuário é obrigatório")

        end_url = self._base_url + username + self._end_url
        response = requests.get(end_url)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        emails_table = soup.find('table', class_='inbox-table')
        
        if not emails_table:
            return []
            
        emails = []
        for row in emails_table.find_all('tr')[1:]:  # Pula o cabeçalho
            email_id = row.get('id')
            cols = row.find_all('td')
            if len(cols) == 3:
                emails.append({
                    'id': email_id,
                    'remetente': cols[0].text.strip(),
                    'assunto': cols[1].text.strip(),
                    'hora': cols[2].text.strip()
                })
                
        return emails
    
    def read_email(self, username: str, email_id: str) -> Dict[str, Any]:
        """
        Lê um email específico da caixa de entrada.
        
        Args:
            username (str): Nome de usuário do email temporário
            email_id (str): ID do email a ser lido
            
        Returns:
            Dict[str, Any]: Dicionário contendo os detalhes do email
            
        Raises:
            ValueError: Se o username não for fornecido ou o email não for encontrado
        """
        if not username:
            raise ValueError("O nome de usuário é obrigatório")
            
        end_url = f"{self._base_url}{username}{self._end_url}#{email_id}"
        response = requests.get(end_url)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        script = soup.find('script', string=lambda t: t and 'var emails = [' in t)
        
        if not script:
            raise ValueError("Email não encontrado")
            
        # Extrai os dados do email do script
        email_data = script.string.split('var emails = [')[1].split('];')[0]
        email = json.loads(f"[{email_data}]")[0]
        
        return {
            'id': email['id'],
            'data': email['created_at'],
            'hora': email['hora'],
            'remetente': email['sender'],
            'email_remetente': email['sender_email'], 
            'destinatario': email['header_to'],
            'assunto': email['header_subject'],
            'corpo': email['body']
        }
    

