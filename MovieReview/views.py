from django.shortcuts import render
from .forms import MovieForm
from .models import MovieInfo
from .filters import MovieInfoFilter
# Create your views here.

def index(request, *args, **qwargs):
        #return HttpResponse('Hello this is view from movie review')
       return render(request, "MovieReview/index.html")

def AddMovie(request):
    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = MovieForm()
    
    context = {
        'form': form
    }
    return render(request, "MovieReview/add_movie.html", context)

def ViewMovie(request):
    queryset = MovieInfo.objects.all()
    context = {
        "object_list": queryset
    }
    
    # context['filter'] = MovieInfoFilter
    return render(request, "MovieReview/view_movie.html", context)

def search(request):
    movie_list = MovieInfo.objects.all()
    movie_filter = MovieInfoFilter(request.GET, queryset= movie_list)
    return render(request, 'MovieReview/movie_list.html', {'filter': movie_filter})

    
