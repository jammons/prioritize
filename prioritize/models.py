from django.contrib.auth.models import User
from django.db import models

class ItemSet(models.Model):
    ''' ItemSet is the model for grouping items together. For example "To Do List" '''
    title = models.CharField(max_length=40, blank=False)
    question = models.CharField(max_length='100', default='Which is more important?',
        help_text='What prompt would you like to show people when they are deciding?')
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

class Item(models.Model):
    ''' Individual items to be compared with a set. '''
    title = models.CharField(max_length=40, blank=False)
    description = models.CharField(max_length=200, blank=True)
    score = models.IntegerField(default=1000, editable=False)
    set = models.ForeignKey(ItemSet, blank=False, null=False, related_name='items')

    def __unicode__(self):
        return self.title
