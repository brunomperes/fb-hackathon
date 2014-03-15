# -*- coding: utf-8 -*-
from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


# Researcher - Participant - Experiment - Application

class UserProfile(models.Model):
    alive = models.BooleanField()
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username

class Game(models.Model):
    users_needed = models.IntegerField()
    ready_users = models.IntegerField()

    def __unicode__(self):
        return self.users_needed
