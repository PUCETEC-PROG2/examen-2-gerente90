from django.template import loader
from django.http import HttpResponse
from .models import Movie
# from django.template import loader

# def index(request):
#     return HttpResponse('Mi primera chamba')

def index(request):
    movies = Movie.objects.all()  #SELECT de Django
    #pokemons = Pokemon.objects.order_by(type)  Esto uso si quiero ordenarlo
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'movies':movies}, request))

def display_movie(request, movie_id):
    #Select where id = pokemon_id
    movie = Movie.objects.get(id=movie_id)
    template = loader.get_template('movie_detail.html')
    context = {
        'movie':movie
    }
    return HttpResponse(template.render(context, request))