from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = "posts/lista_post.html"
    context_object_name = "posts"