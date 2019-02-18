from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class suggest(models.Model):
    sugg_text = models.CharField( max_length=200)
    name_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date submitted')
    def __str__(self):
        return self.sugg_text

    #def was_published_recently(self):
       # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(suggest, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



