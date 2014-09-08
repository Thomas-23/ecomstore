#-- coding: utf-8 --
from django.contrib import admin
from polls.models import Poll
from polls.models import Choice
class ChoiceInline(admin.StackedInline): ##TabularInline扁平化
	model = Choice
	extra = 3
#admin.site.register(Poll)
class PollAdmin(admin.ModelAdmin): 
	fieldsets = [
		(None, {'fields':['question']}),
		('Date information',{'fields':['pub_date'],'classes':['collapse']}),#collapse提供缩放显示
	]
	inlines = [ChoiceInline] #在增加PollAdmin的时候，添加3个内置 Choice对象

admin.site.register(Poll, PollAdmin)


admin.site.register(Choice)
