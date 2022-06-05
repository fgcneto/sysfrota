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

# create superuser
python3 manage.py createsuperuser

# criar arquivos requeriments.txt
pip freeze > ./requirements.txt

# subir e reconstruir os containers dockers web e database
docker-compose up --build