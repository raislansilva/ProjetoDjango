from django.forms import ModelForm
from .models import Transacao,Categoria,Aluno, Curso

class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data','descricao','valor','observacoes','categoria']

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']


class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'curso']


class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'carga_horaria']
