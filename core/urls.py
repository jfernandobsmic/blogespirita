from django.urls import path
from core.views import index, social, citacao, evento, materia, conteudo
from .views import (CentroView, VideoView, MusicaView, LivroView, MensagemView, PCentro, PVideo, PMusica, PLivro,
                    PMensagem)

urlpatterns = [
    path('', index, name='index'),
    path('mensagem', MensagemView.as_view(), name='mensagens'),
    path('musica', MusicaView.as_view(), name='musicas'),
    path('video', VideoView.as_view(), name='videos'),
    path('livro', LivroView.as_view(), name='livros'),
    path('centro', CentroView.as_view(), name='centros'),
    path('evento', evento, name='evento'),
    path('social/<int:id>', social, name='social'),
    path('citacao/<int:id>', citacao, name='citacao'),
    path('materia/<int:id>', materia, name='materia'),
    path('conteudo/<int:id>', conteudo, name='conteudo'),
    path('pcentro', PCentro.as_view(), name='pcentro'),
    path('pvideo', PVideo.as_view(), name='pvideo'),
    path('pmensagem', PMensagem.as_view(), name='pmensagem'),
    path('pmusica', PMusica.as_view(), name='pmusica'),
    path('plivro', PLivro.as_view(), name='plivro'),
]
