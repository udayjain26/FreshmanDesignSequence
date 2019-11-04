from django.contrib import admin
from .models import Events, Tags, Comments
from django.contrib.admin import ModelAdmin
from .forms import EventsForm

# Register your models here.
class EventsAdmin(ModelAdmin):
	form = EventsForm

class TagsAdmin(ModelAdmin):
	model = Tags

class CommentsAdmin(ModelAdmin):
	model = Comments

admin.site.register(Events, EventsAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Comments, CommentsAdmin)
