#-- coding: utf-8 --
from django.contrib import admin
from polls.models import Poll
from polls.models import Choice
class ChoiceInline(admin.TabularInline): #TabularInline扁平化
	model = Choice
	extra = 3
#admin.site.register(Poll)
class PollAdmin(admin.ModelAdmin): 
	fieldsets = [
		(None, {'fields':['question']}),
		('Date information',{'fields':['pub_date'],'classes':['collapse']}),#collapse提供缩放显示
	]
	inlines = [ChoiceInline] #在增加PollAdmin的时候，添加3个内置 Choice对象
	list_display = ('question', 'pub_date','was_published_recently')#列表显示
	list_filter = ['pub_date'] #增加过滤功能
	search_fields = ['question'] #增加一个搜索框
#Change-list pagination, search boxes, filters, date-hierarchies, and column-header-ordering
admin.site.register(Poll, PollAdmin)


admin.site.register(Choice)
