from django.contrib import admin
from portfolio.models import ProjetoWebAPI

class ProjetoWebApiAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'link')
    list_display_links = ('id', 'nome', 'link')


admin.site.register(ProjetoWebAPI, ProjetoWebApiAdmin)
