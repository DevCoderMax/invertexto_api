import requests
from bs4 import BeautifulSoup
from typing import Dict, Any


class person:
    def __init__(self, gender=None, nationality= None):
        self._gender = gender
        self._nationality = nationality
        url = requests.get('https://www.invertexto.com/gerador-de-pessoas').content
        soup = BeautifulSoup(url, 'html.parser')
        person = {
            "dados_pessoais": {
                "nome": soup.find("label", string="Nome").find_next("input")["value"],
                "cpf": soup.find("label", string="CPF").find_next("input")["value"],
                "telefone": soup.find("label", string="Telefone").find_next("input")["value"]
            },
            "nascimento": {
                "data_de_nascimento": soup.find("label", string="Data de Nascimento").find_next("input")["value"],
                "idade": soup.find("label", string="Idade").find_next("input")["value"],
                "signo": soup.find("label", string="Signo").find_next("input")["value"]
            },
            "endereco": {
                "cep": soup.find("label", string="CEP").find_next("input")["value"],
                "endereco": soup.find("label", string="Endereço").find_next("input")["value"],
                "cidade": soup.find("label", string="Cidade").find_next("input")["value"],
                "estado": soup.find("label", string="Estado").find_next("input")["value"]
            },
            "online": {
                "email": soup.find("label", string="E-Mail").find_next("input")["value"],
                "nome_de_usuario": soup.find("label", string="Nome de Usuário").find_next("input")["value"],
                "senha": soup.find("label", string="Senha").find_next("input")["value"]
            },
            "cartao_de_credito": {
                "bandeira": soup.find("label", string="Bandeira").find_next("input")["value"],
                "numero": soup.find("label", string="Número").find_next("input")["value"],
                "expiracao": soup.find("label", string="Expiração").find_next("input")["value"],
                "cvv2": soup.find("label", string="CVV2").find_next("input")["value"]
            },
            "caracteristicas_fisicas": {
                "altura": soup.find("label", string="Altura").find_next("input")["value"],
                "peso": soup.find("label", string="Peso").find_next("input")["value"],
                "tipo_sanguineo": soup.find("label", string="Tipo Sanguíneo").find_next("input")["value"]
            }
        }

        return person