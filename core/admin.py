from django.contrib import admin
from .models import Mensagem, Livro, Musica, Video, Evento, Destaque, Social, Centro, Citacao, Temas


@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'mensagem', 'autor', 'fonte', 'imagem', 'slug']


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'sinopse', 'autor', 'espirito', 'editora', 'ano', 'pdf', 'url', 'imagem', 'slug']


@admin.register(Citacao)
class CiatcaoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'citacao', 'autor', 'livro_id']


@admin.register(Musica)
class MusicaAdmin(admin.ModelAdmin):
    list_display = ['subtitulo', 'descricao', 'cantor', 'compositor', 'ano', 'musica', 'url', 'youtube', 'imagem', 'slug']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['subtitulo', 'descricao', 'autor', 'ano', 'video', 'url', 'youtube', 'imagem', 'slug']


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['evento', 'descricao', 'palestrante', 'endereco', 'bairro', 'cidade', 'cep', 'ano', 'url', 'imagem',
                    'slug']


@admin.register(Destaque)
class DestaqueAdmin(admin.ModelAdmin):
    list_display = ['id_mensagem', 'id_musica', 'id_video', 'id_livro']


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ['atividade', 'descricao', 'dia', 'hora', 'responsavel', 'imagem', 'slug']


@admin.register(Centro)
class CentroAdmin(admin.ModelAdmin):
    list_display = ['nome', 'endereco', 'bairro', 'cidade', 'cep', 'latitude', 'longitude', 'ano', 'url', 'telefone',
                    'imagem', 'slug']

    """def get_social(self, obj):
        for c in Centro.objects.all():
            return ', '.join(s.atividade for s in Social.objects.filter(centro_id=c.id))

    get_social.short_description = 'Social' """


@admin.register(Temas)
class TemasAdmin(admin.ModelAdmin):
    list_display = ['tema', 'subtema', 'descricao', 'imagem']
