from django.contrib import admin
from portfolio.models import ProjetoWebAPI, ProjetoAutomacao

class ProjetoWebApiAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'link')
    list_display_links = ('id', 'nome', 'link')

class ProjetoAutomacaoApiAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'link')
    list_display_links = ('id', 'nome', 'link')


admin.site.register(ProjetoWebAPI, ProjetoWebApiAdmin)
admin.site.register(ProjetoAutomacao, ProjetoAutomacaoApiAdmin)
