from django.urls import path
from api.views import *

app_name = 'api'

urlpatterns = [
    path('', Home.as_view(),name="home"),
    path('personal_loan/', Personal_Loan.as_view(),name="personal_loan"),
    
]
