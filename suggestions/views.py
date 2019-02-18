from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import suggest
from django.template import loader
from django.shortcuts import get_object_or_404,render
from django.http import Http404
from .forms import suggestive
from django.urls import reverse


def detail(request, sugg_id):
    #return HttpResponse("You're looking at suggestions %s." % sugg_id)
    suggestion = get_object_or_404(suggest,pk=sugg_id)
    return render(request, 'suggestions/detail.html', {'suggestion': suggestion})

def list(request):
    return render(request, 'suggestions/list.html',{'suger' : suggest.objects.all()})




def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    latest_suggest_list = suggest.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('suggestions/index.html')
    #output = ', '.join([q.sugg_text for q in latest_suggest_list])
    context = {
        'latest_suggest_list': latest_suggest_list,
    }
    return render(request,'suggestions/index.html',context)



def vote(request,sugg_id):
    #return HttpResponse("You're voting on question %s.")
    suger = get_object_or_404(suggest,pk=sugg_id)
    try:
        select_choice = suger.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request, 'suggestions/sugg.html', {
            'suger': suger,
            'error_message': "You didn't select a choice.",
        })
    else:
        select_choice.choice_text= request.POST['your_sugg']
        select_choice.save()
        return HttpResponseRedirect(reverse('suggestions:results', args=suger.id))


def results(request, suggest_id):
    sug = get_object_or_404(suggest, pk =suggest_id)
    return render(request,'suggestions/results.html',{'sug' : sug})


def get_suggest(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = suggestive(request.POST)

        # check whether it's valid:
        if form.is_valid():
            form.save()
            #sugg=request.POST('your_sugg')
            #name=request.POST('your_name')
            #uggestion_object=suggest(sugg_text=sugg, name_text=name)
            #suggestion_object.save()

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse('Suggestion submitted')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = suggestive()

    return render(request, 'suggestions/sugg.html', {'sug_form': form})