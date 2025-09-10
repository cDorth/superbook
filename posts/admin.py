from django.contrib import admin
from .models import Post, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['autor', 'mensagem_resumida', 'criado_em']
    list_filter = ['autor']
    search_fields = ['autor__codinome', 'mensagem']

    fieldsets = (
        ('Autor do Post', {
            'fields': ('autor',)
        }),
        ('Conteúdo', {
            'fields': ('mensagem',)
        }),
        ('Dados de Registro', {
            'fields': ('criado_em',)
        }),
    )
    readonly_fields = ['criado_em']

    def mensagem_resumida(self, obj):
        return obj.mensagem[:50] + ("..." if len(obj.mensagem) > 50 else "")
    mensagem_resumida.short_description = "Mensagem"


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['heroi', 'post', 'criado_em']
    list_filter = ['heroi', 'post']
    search_fields = ['heroi__codinome', 'post__mensagem']

    fieldsets = (
        ('Informações do Like', {
            'fields': ('heroi', 'post')
        }),
        ('Dados de Registro', {
            'fields': ('criado_em',)
        }),
    )
    readonly_fields = ['criado_em']
