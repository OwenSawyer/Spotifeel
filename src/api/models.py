from django.db import models
from django.db.models import Max
import string
import random

class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.TextField()
    address = models.TextField()

    def __unicode__(self):
        return self.user

    @staticmethod
    def generate_id():
        user_id = User.objects.aggregate(Max('id'))['id__max']
        return user_id + 1

    class Meta:
        db_table = 'table1'
        managed = False

class Url(models.Model):
    shortened = models.TextField(primary_key=True)
    original = models.TextField()

    def __unicode__(self):
        return self.shortened

    @staticmethod
    def generate_id():
        found = True
        while found:
            new_url = 'tophat.ly/'
            for i in range(5):
                new_url += random.choice(string.ascii_letters + string.digits)
            try:
                Url.objects.get(shortened=new_url)
            except Url.DoesNotExist:
                found = False

        return new_url

    class Meta:
        db_table = 'bitly'
        managed = False