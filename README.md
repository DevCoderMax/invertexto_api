Invertexto API (Unofficial)

## Task List

This section outlines the planned and ongoing tasks for the API.

**Notepad**
- [x] **Notepad Creation**
- [x] **Get Content**
- [x] **Set Content**
- [ ] **Support passwords in Notepads**

**IP**
- [x] **Get My IP**
- [x] **Get Local IP Info**

**Temp Mail Service**
- [ ] **Create Random Email**
- [ ] **Create Custom Email**
- [ ] **Get Emails**

      
## Exemplos de Uso

#instalação da biblioteca
```python
pip install git+https://github.com/DevCoderMax/invertexto_api.git
```
#Uso
```python
# cria um notepad
from invertexto_api.modules import Notepad

notepad = Notepad("max")
print(notepad.create())

# pega o conteudo do notepad incluido token pra edição
notepad = Notepad("max")
print(notepad.get_content())

# seta/edita o conteudo do notepad
notepad = Notepad("max")
print(notepad.set_content("testing", 'token'))

# IP

##Captura o meu ip atual
from invertexto_api.modules import ip

meu_ip = IP.my_ip()
print(meu_ip)

# Localização de um ip

ip_test = IP('88.98.134.132')
print(ip_test.LocalIP())

```

