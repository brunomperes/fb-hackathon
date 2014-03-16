# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from myproject.myapp.models import Game, UserProfile
from myproject.myapp.forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login

def user_login(request):
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
                change_alive_status(user.id, True)

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

def register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            user = user_form.save()

            # Once hashed, update the user object.
            user.set_password(user.password)
            user.save()

            registered = True

            user.password = user_form.cleaned_data['password']
            user = authenticate(username=user.username, password=user.password)
            login(request, user)
            return HttpResponseRedirect("/myapp/")

        else:
            print user_form.errors

    else:
        user_form = UserForm()

    return render_to_response(
            'myapp/register.html', {
                        'user_form': user_form, 
                        'registered': registered
                    },
                    context)

def settings(request):
    context = RequestContext(request)

    print 'POST'
    if request.method == 'POST':
        fb_id = request.POST.get('facebook-id')
        print fb_id
        # SHOULD UPDATE ON THE DATABASE THE ID, but we don't know the user.id as it is not authenticated
    
    return render_to_response('myapp/settings.html', {}, context)

def change_alive_status(user_id, status=False):
    user = User.objects.get(id=int(user_id))
    user_profile = UserProfile.objects.get(user=user)
    user_profile.alive = status
    user_profile.save()

@login_required
def user_logout(request):
    change_alive_status(user.id, False)
    logout(request)

    return HttpResponseRedirect('/myapp/')


@login_required
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

@login_required
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

@login_required
def game(request):
    context = RequestContext(request)

    context_dict = {}

    # Checks only the newest entry of the game table
    game = Game.objects.all().reverse()[0]

    target_name = get_user_target(request.user.id)

    context_dict['target_name'] = target_name
    context_dict['target_picture_link'] = 'http://placehold.it/100x100'

    return render_to_response('myapp/game.html', context_dict, context)

@login_required
def death(request):
    context = RequestContext(request)

    user_id = request.POST.get('user_id')

    context_dict = {}

    if request.method == 'POST' and user_id:
        killed_user = UserProfile.objects.get(id=int(user_id))
        killed_user.alive = False
        killed_user.save()

    return render_to_response('myapp/index.html', context_dict, context)

