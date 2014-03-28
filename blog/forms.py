from django import forms
from django_markdown.widgets import MarkdownWidget

class MyCustomForm():
	content = forms.CharField(widget=MarkDownWidget())
