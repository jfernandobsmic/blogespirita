from django.urls import path
from core.views import index, mensagem, social, citacao, evento
from .views import CentroView, VideoView, MusicaView, LivroView, PCentro, PVideo, PMusica, PLivro

urlpatterns = [
    path('', index, name='index'),
    path('mensagem', mensagem, name='mensagens'),
    path('musica', MusicaView.as_view(), name='musicas'),
    path('video', VideoView.as_view(), name='videos'),
    path('livro', LivroView.as_view(), name='livros'),
    path('centro', CentroView.as_view(), name='centros'),
    path('evento', evento, name='evento'),
    path('social/<int:id>', social, name='social'),
    path('citacao/<int:id>', citacao, name='citacao'),
    path('pcentro', PCentro.as_view(), name='pcentro'),
    path('pvideo', PVideo.as_view(), name='pvideo'),
    path('pmusica', PMusica.as_view(), name='pmusica'),
    path('plivro', PLivro.as_view(), name='plivro'),
]
