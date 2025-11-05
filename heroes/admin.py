from django.contrib import admin
from .models import Hero

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ['codinome', 'nome_real', 'email_hero', 'poder_principal', 'cidade', 'criado_em'] # campos exibidos na listagem
    list_filter = ['cidade'] # campo disponivel para filtragem
    search_fields = ['email_hero', 'codinome', 'nome_real', 'cidade'] # campos a serem pesquisados na barra de pesquisa

    fieldsets = ( # divide em seções
        ('Identidade Secreta', {
            'fields': ('codinome', 'nome_real')
        }),
        ('Informações Gerais', {
            'fields': ('email_hero', 'poder_principal', 'cidade', 'historia', 'imagem')
        }),
        ('Dados de Registro', {
            'fields': ('criado_em',),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ['criado_em']