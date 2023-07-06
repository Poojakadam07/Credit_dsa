from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Home(TemplateView):
  template_name = 'index.html'

class Personal_Loan(TemplateView):
  template_name = 'personal_loan.html'
