from django.urls import path
from portfolio.views import index, projeto , contato

urlpatterns = [
        path('', index, name='index'), 
        path('projeto/', projeto, name='projeto'), 
        path('contato/', contato, name='contato'), 
]

