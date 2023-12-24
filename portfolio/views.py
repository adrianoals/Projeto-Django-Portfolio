from django.shortcuts import render
from portfolio.models import ProjetoWebAPI, ProjetoAutomacao

def index(request):
        return render(request, 'portfolio/index.html')

def projeto(request):
        projetos_web_api = ProjetoWebAPI.objects.all()
        projetos_automacoes = ProjetoAutomacao.objects.all()
        return render(request, 'portfolio/projeto.html', {"projetos_web_api": projetos_web_api, "projetos_automacoes" : projetos_automacoes,})

def contato(request):
        return render(request, 'portfolio/contato.html')

