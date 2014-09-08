#-- coding: utf-8 --

from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
#python -c " 查看django源文件存放目录
#import sys
#sys.path = sys.path[1:]
#import django
#print(django.__path__)"

class Poll(models.Model):
	question = models.CharField(max_length=200) 
	pub_date = models.DateTimeField('date published')
	def __unicode__(self): # Python 3: def __str__(self): 
		return self.question
	def was_published_recently(self):
		#return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	#增加was_published_recently的排序功能
	was_published_recently.admin_order_field = 'pub_date' 
	was_published_recently.boolean = True 
	was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=200) 
	votes = models.IntegerField(default=0)
	def __unicode__(self): # Python 3: def __str__(self): 
		return self.choice_text