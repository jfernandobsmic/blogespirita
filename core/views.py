from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Centro, Social, Evento, Musica, Video, Livro, Citacao, Temas


def index(request):
    eventos = Evento.objects.all().order_by('evento').all()
    musicas = Musica.objects.all()
    videos = Video.objects.all()
    eventos = Evento.objects.all()
    centros = Centro.objects.all()
    temas = Temas.objects.all().order_by('tema').all()
    ct_musica = len(musicas)
    ct_video = len(videos)
    ct_evento = len(eventos)
    ct_centro = len(centros)

    return render(request, 'index.html',
                  {'eventos': eventos, 'temas': temas, 'ct_musicas': ct_musica, 'ct_videos': ct_video,
                   'ct_eventos': ct_evento, 'ct_centros': ct_centro})


def mensagem(request):
    return render(request, 'pages/mensagem.html')


def evento(request):
    eventos = Evento.objects.all().orderby('evento').all()
    return render(request, 'evento.html', {'eventos': eventos})


class MusicaView(ListView):
    template_name = 'pages/musicas.html'
    model = Musica
    paginate_by = 3
    ordering = 'cantor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['musicas'] = Musica.objects.all()

        return context


class PMusica(ListView):
    template_name = 'pages/musicas.html'
    model = Musica
    paginate_by = 3
    ordering = 'cantor'

    def get_queryset(self):

        contexto = super().get_queryset()

        opcao = self.request.GET.get('opcao')
        resposta = str(self.request.GET.get('resposta')).capitalize()

        if opcao == '1':
            musica = contexto.filter(ano=resposta).order_by('ano').all()
        elif opcao == '2':
            musica = contexto.filter(cantor__icontains=resposta).all()
        elif opcao == '3':
            musica = contexto.filter(subtitulo__icontains=resposta).all()
        else:
            musica = Video.objects.all().all()

        return musica


class VideoView(ListView):
    template_name = 'pages/videos.html'
    model = Video
    paginate_by = 3
    ordering = 'autor'

    def get_context_data(self, **kwargs):
        context = super(VideoView, self).get_context_data(**kwargs)
        context['videos'] = Video.objects.all()

        return context


class PVideo(ListView):
    template_name = 'pages/videos.html'
    model = Video
    paginate_by = 3
    ordering = 'autor'

    def get_queryset(self):

        contexto = super().get_queryset()

        opcao = self.request.GET.get('opcao')
        resposta = str(self.request.GET.get('resposta')).capitalize()

        if opcao == '1':
            video = contexto.filter(ano=resposta).order_by('ano').all()
        elif opcao == '2':
            video = contexto.filter(autor__icontains=resposta).all()
        elif opcao == '3':
            video = contexto.filter(subtitulo__icontains=resposta).all()
        else:
            video = Video.objects.all().all()

        return video


class LivroView(ListView):
    template_name = 'pages/livros.html'
    model = Livro
    paginate_by = 3
    ordering = 'titulo'

    def get_context_data(self, **kwargs):
        context = super(LivroView, self).get_context_data(**kwargs)
        context['livros'] = Livro.objects.all()

        return context


class PLivro(ListView):
    template_name = 'pages/livros.html'
    model = Livro
    paginate_by = 3
    ordering = 'titulo'

    def get_queryset(self):
        contexto = super().get_queryset()

        opcao = self.request.GET.get('opcao')
        resposta = str(self.request.GET.get('resposta')).capitalize()

        if opcao == '1':
            livro = contexto.filter(titulo__icontains=resposta).all()
        elif opcao == '2':
            livro = contexto.filter(autor__icontains=resposta).all()
        elif opcao == '3':
            livro = contexto.filter(espirito__icontains=resposta).all()
        else:
            livro = Video.objects.all().all()

        return livro


class CentroView(ListView):
    template_name = 'pages/centros.html'
    model = Centro
    paginate_by = 3
    ordering = 'nome'

    def get_context_data(self, **kwargs):
        context = super(CentroView, self).get_context_data(**kwargs)
        context['centros'] = Centro.objects.all().order_by('nome').all()

        return context


class PCentro(ListView):
    template_name = 'pages/centros.html'
    model = Centro
    paginate_by = 3
    ordering = 'nome'

    def get_queryset(self):

        contexto = super().get_queryset()

        opcao = self.request.GET.get('opcao')
        resposta = str(self.request.GET.get('resposta')).capitalize()
        print(opcao)
        print(resposta)

        if opcao == '1':
            centro = contexto.filter(nome=resposta).order_by('nome').all()
        elif opcao == '2':
            centro = contexto.filter(cidade=resposta).order_by('cidade').all()
        elif opcao == '3':
            centro = contexto.filter(bairro=resposta).order_by('bairro').all()
        else:
            centro = Centro.objects.all().order_by('nome').all()

        return centro


def social(request, id):
    at_social = Social.objects.filter(centro__id=id)
    centro = Centro.objects.filter(id=id)
    return render(request, 'pages/social.html', {'centro': centro, 'sociais': at_social})


def citacao(request, id):
    livro = ''
    at_citacao = Citacao.objects.filter(livro_id=id)
    nm_livro = Livro.objects.filter(id=id)
    for l in nm_livro:
        livro = l.titulo
    return render(request, 'pages/citacao.html', {'citacoes': at_citacao, 'livro': livro})
