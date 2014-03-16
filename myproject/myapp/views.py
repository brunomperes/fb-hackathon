# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from myproject.myapp.models import Game, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm

def login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/myapp/')

            else:
                return render_to_response('myapp/login.html', context_dict, context)

        else:
            # Bad login details were provided. So we can't log the user in.
            return render_to_response('myapp/login.html', context_dict, context)

    else:
        return render_to_response('myapp/login.html', {}, context)

def list(request):
    context = RequestContext(request)
    return render_to_response('myapp/settings.html', {}, context)

def settings(request):
    context = RequestContext(request)

    if request.method == 'POST':
        fb_name = request.POST.get('facebook-id')

        print request.POST.get('facebook-id')
        print request.POST.get('facebook-name')


    
    return render_to_response('myapp/settings.html', {}, context)

@login_required
def user_logout(request):

    logout(request)

    return HttpResponseRedirect('/myapp/')


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

    return HttpResponse(game.ready_users - game.users_needed)

def get_user_target(user_id=None):
    ## ADD ADAM FUNCTION HERE
    return 'Bruno Peres'

#@login_required
def game(request):
    context = RequestContext(request)

    context_dict = {}

    # Checks only the last entry of the game table
    game = Game.objects.all().reverse()[0]

    target_name = get_user_target(request.user.id)

    context_dict['target_name'] = target_name

    return render_to_response('myapp/game.html', context_dict, context)

#@login_required
def death(request):
    context = RequestContext(request)

    user_id = request.POST.get('user_id')

    context_dict = {}

    if request.method == 'POST' and user_id:
        killed_user = UserProfile.objects.get(id=int(user_id))
        killed_user.alive = False
        killed_user.save()

    return render_to_response('myapp/index.html', context_dict, context)

