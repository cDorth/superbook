from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
    path('cbv-lista/', PostListView.as_view(), name='cbv_lista_post'),
]

# do carlos