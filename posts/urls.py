from django.urls import path
from . import views
from .views import PostList, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('lista/', PostList.as_view(), name="lista_posts"),
    path('novo/', PostCreateView.as_view(), name='novo_post'),
    path('<int:pk>/editar/', PostUpdateView.as_view(), name='editar_post'),
    path('<int:pk>/excluir/', PostDeleteView.as_view(), name='excluir_post'),
    path('<int:id>/detail_posts/', views.postDetail, name='info_post'),
]

# Gabriel Morais