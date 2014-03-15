# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from myproject.myapp.models import Game, UserProfile
from django.contrib.auth.models import User

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm

def login(request):
    if request.method == 'POST':
        print "post"
        form = DocumentForm(request.POST)
        print form.data
        return render_to_response(
                'myapp/login.html',
                {})
    else:
        return render_to_response(
                'myapp/login.html',
                {})

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'myapp/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )


#@login_required
def index(request):
    context = RequestContext(request)

    alive_users = UserProfile.objects.filter(alive=True)
    dead_users = UserProfile.objects.filter(alive=False)

    # FIXME
    if Game.objects.all().count() == 0:
        game = Game(ready_users=0, users_needed=2)
        game.save()

    context_dict = {}

    context_dict['alive_users'] = alive_users
    context_dict['dead_users'] = dead_users

    return render_to_response('myapp/index.html', context_dict, context)

#@login_required
def ready(request):
    context = RequestContext(request)

    # Checks only the last entry of the game table
    game = Game.objects.all().reverse()[0]
    
    if request.GET.get('data-user-id'):
        game.ready_users += 1
        game.save()

    print game.ready_users

    if game.ready_users >= game.users_needed:
        return HttpResponse('True')

    return HttpResponse('False')

def get_user_target(user_id=None):
    ## ADD ADAM FUNCTION
    return User.objects.all()[0]

#@login_required
def game(request):
    context = RequestContext(request)

    

    # Checks only the last entry of the game table
    game = Game.objects.all().reverse()[0]

    print game.ready_users

    game.ready_users += 1
    game.save()

    if game.ready_users >= game.users_needed:
        HttpResponseRedirect('/myapp/game')
    else:
        HttpResponseRedirect('/myapp/index')

    return render_to_response('myapp/ready.html', context_dict, context)