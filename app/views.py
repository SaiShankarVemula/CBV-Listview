from django.shortcuts import render
from app.models import *
from django.views.generic import View,TemplateView,FormView,ListView
# Create your views here.


class Trainer_list(ListView):
    template_name='Trainer_list.html'
    model=Trainer
    context_object_name="trainer"
