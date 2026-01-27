from django.db import models
from stdimage.models import StdImageField
import uuid


def get_file_path_musica(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'musica/{uuid.uuid4()}.{ext}'
    return filename


def get_file_path_video(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'video/{uuid.uuid4()}.{ext}'
    return filename


def get_file_path_livro(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'livro/{uuid.uuid4()}.{ext}'
    return filename


def get_file_path_icone(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'icon/{uuid.uuid4()}.{ext}'
    return filename


def get_file_path_social(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'social/{uuid.uuid4()}.{ext}'
    return filename


def get_file_path_tema(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'tema/{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Mensagem(Base):
    titulo = models.CharField('Titulo', max_length=100)
    mensagem = models.TextField('Mensagem', max_length=500)
    autor = models.CharField('Autor', max_length=60)
    fonte = models.CharField('Fonte', max_length=100)
    imagem = StdImageField('Imagem', upload_to='media', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    class Meta:
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'

    def __str__(self):
        return self.titulo


class Livro(Base):
    titulo = models.CharField('Titulo', max_length=100)
    sinopse = models.TextField('Sinopse', max_length=500)
    autor = models.CharField('Autor', max_length=60)
    espirito = models.CharField('Espirito', max_length=100)
    editora = models.CharField('Editora', max_length=50)
    ano = models.CharField('Ano', max_length=4)
    pdf = models.FileField('Pdf', upload_to=get_file_path_livro, blank=True)
    url = models.URLField('Url', max_length=100)
    imagem = StdImageField('Imagem', upload_to='media', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.titulo


class Citacao(Base):
    titulo = models.CharField('Titulo', max_length=255)
    citacao = models.TextField('Citacao', max_length=500)
    autor = models.CharField('Autor', max_length=100, blank=True)
    livro_id = models.ForeignKey('core.Livro', verbose_name='Livro', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Citação'
        verbose_name_plural = 'Citações'

    def __str__(self):
        return self.titulo


class Musica(Base):
    subtitulo = models.CharField('Subtitulo', max_length=100)
    descricao = models.TextField('Descricao', max_length=500)
    cantor = models.CharField('Cantor', max_length=100)
    compositor = models.CharField('Compositor', max_length=100)
    ano = models.CharField('Ano', max_length=4)
    musica = models.FileField('Musica', upload_to=get_file_path_musica, blank=True)
    url = models.URLField(max_length=100, blank=True)
    youtube = models.URLField(max_length=150, blank=True)
    imagem = StdImageField('Imagem', upload_to='media', variations={'thumb': (400, 400)}, blank=True)
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    class Meta:
        verbose_name = 'Música'
        verbose_name_plural = 'Músicas'

    def __str__(self):
        return self.subtitulo


class Video(Base):
    subtitulo = models.CharField('Subtitulo', max_length=100)
    descricao = models.TextField('Descricao', max_length=500)
    autor = models.CharField('Autor', max_length=100)
    ano = models.CharField('Ano', max_length=4)
    video = models.FileField('Video', upload_to=get_file_path_video, blank=True)
    url = models.URLField('Url', max_length=100, blank=True)
    youtube = models.URLField(max_length=150, blank=True)
    imagem = StdImageField('Imagem', upload_to='media', variations={'thumb': (400, 400)}, blank=True)
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    class Meta:
        verbose_name = 'Vídeo'
        verbose_name_plural = 'Vídeos'

    def __str__(self):
        return self.subtitulo


class Evento(Base):
    evento = models.CharField('Evento', max_length=100)
    descricao = models.TextField('Descricao', max_length=500)
    palestrante = models.CharField('Palestrante', max_length=100)
    endereco = models.CharField('Endereço', max_length=200)
    bairro = models.CharField('Bairro', max_length=60)
    cidade = models.CharField('Cidade', max_length=100)
    cep = models.CharField('CEP', max_length=50)
    ano = models.CharField('Ano', max_length=4)
    url = models.URLField('Url', max_length=100)
    imagem = StdImageField('Imagem', upload_to='media', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.evento


class Destaque(Base):
    id_mensagem = models.ForeignKey('core.Mensagem', verbose_name='Mensagem', on_delete=models.CASCADE)
    id_musica = models.ForeignKey('core.Musica', verbose_name='Musica', on_delete=models.CASCADE)
    id_video = models.ForeignKey('core.Video', verbose_name='Video', on_delete=models.CASCADE)
    id_livro = models.ForeignKey('core.Livro', verbose_name='Livro', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Destaque'
        verbose_name_plural = 'Destaques'

    def __str__(self):
        return f'{self.id_mensagem}, {self.id_musica}, {self.id_video}, {self.id_musica}'


class Social(Base):
    atividade = models.CharField('Atividade', max_length=150, blank=True)
    descricao = models.TextField('Descrição', max_length=500, blank=True)
    dia = models.CharField('Dia', max_length=250,  blank=True)
    hora = models.CharField('Hora', blank=True)
    responsavel = models.CharField('Resposável', max_length=100, blank=True)
    contato = models.CharField('Contato', max_length=20, blank=True)
    icon = models.ImageField(upload_to=get_file_path_icone, blank=True)
    imagem = StdImageField('Imagem', upload_to=get_file_path_social, variations={'thumb': (400, 400)}, blank=True)
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Sociais'

    def __str__(self):
        return self.atividade


class Centro(Base):
    nome = models.CharField('Nome', max_length=150)
    endereco = models.CharField('Endereço', max_length=200)
    bairro = models.CharField('Bairro', max_length=60)
    cidade = models.CharField('Cidade', max_length=100)
    cep = models.CharField('CEP', max_length=50, blank=True)
    latitude = models.DecimalField('Latitude', max_digits=12, decimal_places=6, default=0, blank=True)
    longitude = models.DecimalField('Longitude', max_digits=12, decimal_places=6, default=0,  blank=True)
    ano = models.CharField('Ano', max_length=4, blank=True)
    missao = models.TextField('Missao', max_length=400, blank=True)
    url = models.URLField('Url', max_length=100, blank=True)
    telefone = models.CharField('Telefone', max_length=25, blank=True)
    instagram = models.URLField('Instagram', max_length=100, blank=True)
    facebook = models.URLField('Facebook', max_length=100, blank=True)
    youtube = models.URLField('Youtube', max_length=100, blank=True)
    imagem = StdImageField('Imagem', upload_to='media', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
    evento = models.ManyToManyField(Evento, blank=True)
    social = models.ManyToManyField(Social, blank=True)

    class Meta:
        verbose_name = 'Centro'
        verbose_name_plural = 'Centros'

    def __str__(self):
        return self.nome


class Temas(Base):
    tema = models.CharField('Tema', max_length=50)
    subtema = models.CharField('Subtema', max_length=250)
    descricao = models.TextField('Descricao', max_length=500)
    imagem = StdImageField('Imagem', upload_to=get_file_path_tema)

    class Meta:
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'

    def __str__(self):
        return self.tema

