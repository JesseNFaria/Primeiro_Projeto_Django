from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self):
        return self.nome
        #return f'{self.nome} QTD Estoque: {self.estoque}'

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=150)
    email = models.EmailField('E-mail',max_length=100)
    data_nascimento = models.DateTimeField('Data de Nascimento')

    def __str__(self):
        return self.nome