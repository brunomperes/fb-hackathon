import os

# Definig population script
def populate():
    #Adding a Researcher
    user_mickey = add_user(username='mick',
                first_name='Mickey',
				email='pashov.m@gmail.com',
				password='1234',
                is_active=True)

    mickey = add_userprofile(alive=True,
                user=user_mickey)

    #another researcher

    user_goofy = add_user(username='goofy',
                        first_name='Goofy',
                        email='goofy@disney.com',
                        password='1234',
                        is_active=True)

    goofy = add_userprofile(alive=True,
                           user=user_goofy)
    #another researcher

    user_don = add_user(username='don',
                        first_name='Vito Corleone',
                        email='donvito@littleitaly.com',
                        password='1234',
                        is_active=True)

    don = add_userprofile(alive=True,
                         user=user_don)

    # Adding a Participant

    user_bruno = add_user(username = 'bruno',
            first_name = 'Bruno',
			email = 'bruno@developer.com',
			password = '1234',
            is_active=True)

    bruno = add_userprofile(
     		alive = True,
            user = user_bruno)

    # another participant

    user_vader = add_user(username='lord_vader',
                           first_name='Anakin Skywalker',
                           email='vadder@republic.sith.galaxy',
                           password='1234',
                           is_active=True)

    vadder = add_userprofile(
     		alive = True,
            user = user_vader)


# Defining the add functions for our models
def add_user(username, first_name, email, password, is_active):

    u = User.objects.get_or_create(username = username, first_name = first_name, email = email, password = password, is_active = is_active, fb_id='1', hunts_fb_id='1')[0]
    u.set_password(password)
    u.save()
    return u

def add_userprofile(alive, user):

    r = UserProfile.objects.get_or_create(alive = alive, user = user)[0]
    return r


# Start execution here!
if __name__ == '__main__':
    print "Starting MaxiMatch population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    from myproject.myapp.models import UserProfile
    from django.contrib.auth.models import User
    populate()
