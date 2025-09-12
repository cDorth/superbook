from django.contrib import admin
from .models import Villain

@admin.register(Villain)
class VillainAdmin(admin.ModelAdmin):
    list_display = ['codinome', 'nome_real', 'poder_principal', 'cidade', 'criado_em'] # campos exibidos na listagem
    list_filter = ['cidade'] # campo disponível para filtrar os dados
    search_fields = ['codinome', 'nome_real', 'cidade'] # campos a serem pesquisados na barra de pesquisa

    fieldsets = ( # divide em seções 
        ('Identidade Secreta', {
            'fields': ('codinome', 'nome_real')
        }),
        ('Informações Gerais', {
            'fields': ('poder_principal', 'cidade', 'historia')
        }),
        ('Dados de Registro', {
            'fields': ('criado_em',)
        }),
    )
    readonly_fields = ['criado_em']