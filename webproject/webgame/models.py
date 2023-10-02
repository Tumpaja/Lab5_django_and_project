from django.db import models

# Create your models here.
'''
class Game(models.Model):
    name = models.CharField(max_length=100)
    type = models.charField(max_length=100)

    class Meta:
        verbose_name_pural = "Game"

        def _str_(self):
            return self.name
'''
class Question(models.Model):
    question = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    
