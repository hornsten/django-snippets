from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponseRedirect, Http404
from .models import Snippet
from django.core.urlresolvers import reverse


# Create your views here.

# def index(request):
#     snippets = Snippet.objects.all()
#     context = {'snippets': snippets}
#     return render(request, 'snippets/index.html', context)

def add(request):
    if request.method == 'POST':
        # save dat data
        Snippet(
            title=request.POST['title'],
            language=request.POST['language'],
            description=request.POST['description'],
            snippet=request.POST['snippet']
        ).save()

    return render(request, 'snippets/add.html', {})

def update_snippet(request,pk):

    Snippet(
        title=request.POST("title"),
        language=request.POST("language"),
        snippet=request.POST("snippet"),
        description=request.POST("description")
        ).save()
        
    return render(request, 'snippets/home.html')

def delete_snippet(request, pk):
    snippet = Snippet.objects.get(pk=pk)
    context = { 'snippet': snippet }
    snippet.delete()

    return render(request,'snippets/delete_snippet.html', context)

def home(request):
    snippets = Snippet.objects.all()
    context = {'snippets': snippets}
    return render(request, 'snippets/home.html', context)

# class DetailView(generic.DetailView):
#     model=Snippet
#     template_name = 'snippets/detail.html'

def detail(request, snippet_id):
    try:
        snippet = Snippet.objects.get(id=snippet_id)
        context = { 'snippet': snippet  }
    except Snippet.DoesNotExist:
        raise Http404('Aint no snippet by that id!')

    return render(request, 'snippets/detail.html', context)
