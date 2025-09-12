from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import PostForm
from django.urls import reverse_lazy
from comments.forms import ComentarioForm

# Create your views here.
class PostList(ListView):
    model = Post
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('lista_posts')

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('lista_posts')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/confirmar_exclusao.html'
    success_url = reverse_lazy('lista_posts')

def postDetail(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        comentario = ComentarioForm(request.POST)
        if comentario.is_valid():
            comentario = comentario.save(commit=False)
            comentario.id_post = post   
            comentario.save()
            return redirect('info_post', id=id)  
    else:
        comentario = ComentarioForm()

    return render(request, 'posts/detail_posts.html', {
        'detail_post': post,
        'form': comentario
    })

# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'posts/detail_posts.html'
#     context_object_name = 'info_post'

