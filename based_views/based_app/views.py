# coding: utf-8
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import RedirectView, TemplateView
from django.http import HttpResponse
from .models import Poem
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone
from .forms import PoemModelForm

# Create your views here.
class MyView(View):
	def get(self, request, *args, **kwargs):
		return HttpResponse("Hello World!!!")

class AddModelView(View):
	def get(self, request):
		return render(request, 'add.html', {'form':PoemModelForm()}) 
	
	def post(self, request):
		form = PoemModelForm(request.POST)
		form.save()
		return render(request, 'success.html')

class HomePageView(TemplateView):
	template_name = 'home.html'
	def get_context_data(self, **kwargs):
		context = super(HomePageView, self).get_context_data(**kwargs)
		context['poems'] = Poem.objects.all()[:5]
		return context

class PoemCounterRedirectView(RedirectView):
	pattern_name = 'details'	
	def get_redirect_url(self, *args, **kwargs):
		poem = get_object_or_404(Poem, pk=kwargs['pk'])
		poem.update_counter()
		poem.save()
		return super(PoemCounterRedirectView, self).get_redirect_url(*args, **kwargs)

class PoemDetailView(DetailView):
	model = Poem
	template_name = 'detail.html'
		
	def get_context_data(self, **kwargs):
		context = super(PoemDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

class PoemListView(ListView):
	model = Poem
	template_name = 'list.html'

	def get_context_data(self, **kwargs):
		context = super(PoemListView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context
def home(request):
	for poem in Poem.objects.all():
		poem.slug = poem.title
		poem.save()
		print(poem.slug)
	poem = Poem.objects.get(title='静夜思')
	return render(request, 'home.html', {'poems':Poem.objects.all(),'count':poem.count})

		
