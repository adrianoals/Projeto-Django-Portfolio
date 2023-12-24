from django.contrib import admin
from portfolio.models import ProjetoWebAPI, ProjetoAutomacao, ProjetoMobile

class ProjetoWebApiAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'link')
    list_display_links = ('id', 'nome', 'link')

class ProjetoAutomacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'link')
    list_display_links = ('id', 'nome', 'link')

class ProjetoMobileAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'link')
    list_display_links = ('id', 'nome', 'link')


admin.site.register(ProjetoWebAPI, ProjetoWebApiAdmin)
admin.site.register(ProjetoAutomacao, ProjetoAutomacaoAdmin)
admin.site.register(ProjetoMobile, ProjetoMobileAdmin)
