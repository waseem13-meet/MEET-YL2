from django.db import models

# Create your models(classes) here.

class Poll(models.Model):
	question=models.CharField(max_length=200)
class Choice(models.Model):
	choice=models.CharField(max_length=200)
	poll=models.ForeignKey(Poll)


