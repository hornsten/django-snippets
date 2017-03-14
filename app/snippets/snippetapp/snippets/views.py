from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, Http404
from .models import Snippet
from django.core.urlresolvers import reverse_lazy

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

def delete_snippet(request, pk):
    snippet = Snippet.objects.get(pk=pk)
    context = { 'snippet': snippet }
    snippet.delete()

    return render(request,'snippets/delete_snippet.html', context)

def home(request):
    snippets = Snippet.objects.all()
    context = {'snippets': snippets}
    return render(request, 'snippets/home.html', context)

class SnippetUpdate(UpdateView):
    model = Snippet
    fields = ['title','language','description','snippet']
    success_url = reverse_lazy('snippets:home')

# class SnippetCreate(CreateView):
#     model = Snippet
#     fields = ['title','language','description','snippet']

# class SnippetDelete(DeleteView):
#     model = Snippet
#     success_url = reverse_lazy('snippets:home')

def detail(request, snippet_id):
    try:
        snippet = Snippet.objects.get(id=snippet_id)
        context = { 'snippet': snippet  }
    except Snippet.DoesNotExist:
        raise Http404('Aint no snippet by that id!')

    return render(request, 'snippets/detail.html', context)
