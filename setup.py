from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line and not line.startswith('#')]


setup(
    name="invertexto_api",  # Nome do pacote
    version="0.1.0",        # Versão do pacote
    description="Uma API não oficial para invertexto",  # Breve descrição do projeto
    author="Gleyson Carvalho",      
    author_email="gleysondonascimentocarvalho@gmail.com",  
    url="https://github.com/DevCoderMax/invertexto_api",  
    packages=find_packages(),  
    install_requires=[         # Dependências do seu projeto
        "fastapi",
        "uvicorn",
        "pydantic",
        *parse_requirements('requirements.txt')
    ],
    classifiers=[             # Classificadores para o projeto
        "Programming Language :: Python :: 3",
        "Framework :: FastAPI",
        "License :: OSI Approved :: MIT License",  # ou outra licença que você escolher
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',  # Versão mínima do Python
)
