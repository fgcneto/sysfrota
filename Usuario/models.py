from django.db import models
from django.contrib.auth.models import User
from cpf_field.models import CPFField

class Usuario(User):
  
  cpf = CPFField('cpf', unique=True)


  def __str__(self):
      return self.first_name + " " + self.last_name

  class Meta:
      ordering = ['first_name', 'last_name']
      verbose_name = "Usuário"
      verbose_name_plural = "Usuários"

