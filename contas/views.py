from django.shortcuts import render
from django.http import HttpResponse
from .models import Transacao, Categoria,Aluno,Curso
from .form import TransacaoForm, CategoriaForm, AlunoForm, CursoForm
from django.shortcuts import redirect


import datetime

def home(request):
    data = {}
    data['transacoes'] = ['t1','t2','t3']
    data['now'] = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'contas/home.html', data)

def novaTrasacao(request):
    data ={}
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    return render(request, 'contas/form.html', data)


def listagem(request):
    data = {}
    data['transacoes'] = Curso.objects.all()
    return render(request, 'contas/listagem.html', data)


def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance = transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'contas/form.html', data)


def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')


def categoria(request):
    data = {}
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    return render(request, 'contas/form.html', data)



def createAluno(request):
    data = {}
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    return render(request, 'contas/form.html', data)

def createCurso(request):
    data = {}
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    return render(request, 'contas/form.html', data)





