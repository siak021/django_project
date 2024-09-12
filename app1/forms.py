
from app1.models import Topic,Entry
from django.forms import ModelForm
from django import forms

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}
        wigets = {'text' : forms.Textarea(attrs={'cols':80})}


class EntrieForm(ModelForm):
    class Meta:
        model  =Entry
        fields = ['text']
        labels = {'text':''}
        wigets = {'text' : forms.Textarea(attrs={'cols':80})}
