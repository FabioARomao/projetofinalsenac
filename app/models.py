from django.db import models
from datetime import datetime

class Pessoa(models.Model):
  id = models.AutoField(primary_key=True)
  nomne = models.CharField(max_length=255)
  sobrenome = models.CharField(max_length=255)
  cpf = models.CharField(max_length=255)
  endereco = models.CharField(max_length=255)

class Produto(models.Model):
  id = models.AutoField(primary_key=True)
  nome = models.CharField(max_length=255)
  preco = models.CharField(max_length=255)
  quantidade = models.CharField(max_length=255)
  descricao = models.CharField(max_length=255)

class Login(models.Model):
  id = models.AutoField(primary_key=True)
  email = models.CharField(max_length=255)
  passowrd = models.CharField(max_length=255)

class Signup(models.Model):
  id = models.AutoField(primary_key=True)
  email = models.CharField(max_length=255)
  nome = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  
