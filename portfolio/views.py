from django.shortcuts import render
from portfolio.models import ProjetoWebAPI

def index(request):
        return render(request, 'portfolio/index.html')

def projeto(request):
        projetos = ProjetoWebAPI.objects.all()
        return render(request, 'portfolio/projeto.html', {"projetos": projetos})

def contato(request):
        return render(request, 'portfolio/contato.html')

