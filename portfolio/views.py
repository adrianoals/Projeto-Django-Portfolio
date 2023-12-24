from django.shortcuts import render, redirect
from portfolio.models import ProjetoWebAPI, ProjetoAutomacao, ProjetoMobile
from portfolio.forms import ContatoForm
from django.contrib import messages
from django.core.mail import send_mail


def index(request):
        return render(request, 'portfolio/index.html')

def projeto(request):
        projetos_web_api = ProjetoWebAPI.objects.all()
        projetos_automacoes = ProjetoAutomacao.objects.all()
        projetos_mobile = ProjetoMobile.objects.all()
        return render(request, 'portfolio/projeto.html', {"projetos_web_api": projetos_web_api, "projetos_automacoes" : projetos_automacoes, "projetos_mobile" : projetos_mobile, })

# def contato(request):
#         return render(request, 'portfolio/contato.html')

# def contato(request):
#     if request.method == 'POST':
#         form = ContatoForm(request.POST)
#         if form.is_valid():
#             # Processar o formulário
#             nome = form.cleaned_data['nome']
#             email = form.cleaned_data['email']
#             assunto = form.cleaned_data['assunto']
#             mensagem = form.cleaned_data['mensagem']

#             # Enviar e-mails para você
#             send_mail(
#                  f'Novo Contato - {assunto}',
#                  f'Nome: {nome}\nEmail: {email}\n\nMensagem:\n{mensagem}','adrianotesteapp@gmail.com',  # E-mail remetente
#                  ['dri.limasantos@gmail.com'], # E-mail destinatario  
#                  fail_silently=False,
#                  )

#             # Adicionar mensagem de sucesso
#             messages.success(request, 'Mensagem enviada com sucesso!')

#     else:
#         form = ContatoForm()

#     return render(request, 'portfolio/contato.html', {'form': form})


def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            # Processar o formulário
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            # Enviar e-mails para você
            send_mail(
                 f'Novo Contato - {assunto}',
                 f'Nome: {nome}\nEmail: {email}\n\nMensagem:\n{mensagem}','adrianotesteapp@gmail.com',  # E-mail remetente
                 ['dri.limasantos@gmail.com'], # E-mail destinatario  
                 fail_silently=False,
                 )

            # Adicionar mensagem de sucesso
            messages.success(request, 'Mensagem enviada com sucesso!')

            # Redirecionar para a mesma página após o POST bem-sucedido
            return redirect('contato')

    else:
        form = ContatoForm()

    return render(request, 'portfolio/contato.html', {'form': form})
