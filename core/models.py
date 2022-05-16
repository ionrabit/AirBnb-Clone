from django.db import models

class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #Abstract Model is not saved in DB 
    class Meta:
        abstract = True