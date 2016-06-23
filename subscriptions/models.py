from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SubscriptionPost(models.Model):
	date_created = models.DateTimeField('date created')
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	rules = models.CharField(max_length=500)
	category = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	recurring = models.BooleanField(default=True)					# Will this subscription be charged periodically
	recurring_period = models.IntegerField(default=1)				# Months
	subscriptions_available = models.IntegerField(default=1)


#class Question(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')



#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)