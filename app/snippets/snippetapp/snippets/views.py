from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from .models import Snippet
# Create your views here.
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

def home(request):
    snippets = Snippet.objects.all()
    context = {'snippets': snippets}
    return render(request, 'snippets/home.html', context)

def detail(request, snippet_id):
    try:
        snippet = Snippet.objects.get(id=snippet_id)
        context = { 'snippet': snippet  }
    except Snippet.DoesNotExist:
        raise Http404('Aint no snippet by that id!')

    return render(request, 'snippets/detail.html', context)
