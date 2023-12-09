from django.shortcuts import render

def index(request):
        return render(request, 'portfolio/index.html')

def projeto(request):
        return render(request, 'portfolio/projeto.html')

def contato(request):
        return render(request, 'portfolio/contato.html')

