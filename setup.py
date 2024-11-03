from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line and not line.startswith('#')]


setup(
    name="invertexto_api",  
    version="0.1.0",        
    description="Uma API não oficial para invertexto",  
    author="Gleyson Carvalho",      
    author_email="gleysondonascimentocarvalho@gmail.com",  
    url="https://github.com/DevCoderMax/invertexto_api",  
    packages=find_packages(),
    install_requires=[         
        "requests",
        "bs4",
        *parse_requirements('requirements.txt')
    ],
    classifiers=[             
        "Programming Language :: Python :: 3",
        "Framework :: FastAPI",
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10', 
)
