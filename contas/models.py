from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7,decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField()

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = 'Transações'



class Curso(models.Model):
    nome = models.CharField(max_length=200)
    carga_horaria = models.IntegerField()
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    dt_criacao = models.DateTimeField(auto_now_add=True)
    curso = models.ManyToManyField(Curso)

    def __str__(self):
        return self.nome






