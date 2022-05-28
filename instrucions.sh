## instalar ambiente virtual
python venv venv

# ativar ambiente virtual
source ./venv/bin/activate
# atualiazar bibliotecas
pip install pip setuptools wheel -upgrade

# instalar Django dentro do ambiente virtual
pip3 install Django

# criar projeto Django 
django-admin startproject sysfrota .

# criar app
python manage.py startapp SeuApp

#  iniciar projeto Django
python manage.py runserver

# install pip CPF Field
pip install django-cpf