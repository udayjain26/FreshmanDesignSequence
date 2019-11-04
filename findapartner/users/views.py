
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def home(request):
	return render(request,"index.html")
def faqpage(request):
	return render(request, "faqpage.html")
def contactpage(request):
	return render(request, "contactpage.html")

# Create your views here.
