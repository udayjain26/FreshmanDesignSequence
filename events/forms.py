from .models import Events, Tags, Comments
from django import forms

class EventsForm(forms.ModelForm):
	class Meta:
		model = Events
		fields = '__all__'

class NewEventsForm(forms.ModelForm):
	class Meta:
		model = Events
		fields = ('title', 'location', 'eventDate', 'eventTime', 'description', 'image', 'tags')

class CommentsForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ('name',)
