from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
