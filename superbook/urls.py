from django.contrib import admin

admin.site.site_header = "SuperBook Admin"
admin.site.site_title = "SuperBook Painel"
admin.site.index_title = "Bem-vindo ao SuperBook"

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('heroes/', include('heroes.urls')),  # rotas do app heroes
    path('posts/', include('posts.urls')),    # rotas do app posts
]
