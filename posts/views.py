from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView
from .forms import PostsForm

# Create your views here.
def lista_posts(request):
    posts = Post.objects.all()  # busca todos os heróis do banco
    return render(request, "posts/lista_posts.html", {"posts": posts})

class PostListView(ListView):
    model = Post
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"

def criar_post(request):
    if request.method == "POST":
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostsForm()

    return render(request, "posts/form_posts.html", {"form": form})