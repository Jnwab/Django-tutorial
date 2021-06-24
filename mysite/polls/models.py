
import datetime

from django.db import models #importing models, simple.
from django.utils import timezone #IMported timezone, like  actual TIME managment.

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200) #CharField is meant to just represent strings taht are written out.
    pub_date = models.DateTimeField('date published') #DateTimeField seems to be the storage of data
    
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >+ timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text