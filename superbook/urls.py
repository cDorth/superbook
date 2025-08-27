from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('heroes/', include('heroes.urls')),  # rotas do app heroes
    path('posts/', include('posts.urls')),    # rotas do app posts
]