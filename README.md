
# Ação Vida - Sistema de Doações

## Sobre o projeto

Sistema web desenvolvido como MVP acadêmico para auxiliar a ONG Ação Vida no cadastro, na organização e no acompanhamento de doações.

## Objetivo

Facilitar o registro das doações recebidas, armazenando informações sobre responsáveis, materiais, quantidades e datas.

## Funcionalidades

- Menu inicial.
- Cadastro de doações.
- Identificação do responsável.
- Classificação dos materiais.
- Registro de quantidade e unidade de medida.
- Consulta ao histórico de doações.

## Tecnologias utilizadas

- Python
- Django
- SQLite
- HTML
- CSS
- Git e GitHub

## Como executar

1. Instale o Python.
2. Clone o repositório.
3. Crie um ambiente virtual:

   python -m venv venv

4. Ative o ambiente virtual:

   .\venv\Scripts\Activate.ps1

5. Instale as dependências:

   pip install -r requirements.txt

6. Execute as migrações:

   python manage.py migrate

7. Inicie o servidor:

   python manage.py runserver

8. Acesse http://127.0.0.1:8000/
# acao-vida-sistema-doacoes
