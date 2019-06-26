from django.shortcuts import render,get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import bitlyform, editbitly
from .models import bitly
# Create your views here.

from .utils import create_shortcode

def index(request):
    qs = bitly.objects.all()
    context = {"objs": qs}

    return render(request, "index.html", context)

def create(request):   
    form = bitlyform(request.POST or None)
 
    if form.is_valid():
        instance = form.save(commit=False)

        instance.shortcode = create_shortcode()
        instance.datewise = "{}"

        instance.save()

        return HttpResponseRedirect("http://127.0.01:8000/home/")

    context = { "urlform":form}

    return render( request,"create.html",context)
        
def goto (request, shortcode=None):
    qs = get_object_or_404(bitly, shortcode__iexact=shortcode)
    from .utils import current_date
    import json
    instance = json.loads(qs.datewise)
    crt_date = current_date()
    if crt_date in instance:

        instance[crt_date] +=1
    else:
        instance[crt_date] = 1
    qs.datewise = json.dumps(instance)
    qs.save()
    return HttpResponseRedirect(qs.long_url)

def update (request,id=None):
    qs = get_object_or_404(bitly,id=id)                        
    form = editbitly(request.POST or None, instance=qs)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("http://127.0.0.1:8000/home")

    context = {'urlform':form}
    return render(request,"create.html",context)

def delete(request,id=None):
    qs = get_object_or_404(bitly,id=id)
    qs.delete()
    return HttpResponseRedirect("http://127.0.0.1:8000/home")
