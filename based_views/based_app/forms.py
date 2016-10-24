from django import forms
from .models import Poem

class PoemModelForm(forms.ModelForm):
	class Meta:
		model = Poem
		fields = ['title', 'author']
