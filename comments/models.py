from django.db import models
from posts.models import Post
from heroes.models import Hero

# Create your models here.
class Comentario(models.Model):
    conteudo = models.CharField(max_length=300)
    id_autor = models.ForeignKey(Hero, on_delete=models.CASCADE)
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

