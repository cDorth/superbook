from django.urls import path
from .views import *

urlpatterns = [
    path('lista/', lista_posts, name='lista_posts'),
    path('cbv-lista/', PostListView.as_view(), name='cbv_lista_posts'),
    path('novo/', criar_post, name='criar_posts')
]