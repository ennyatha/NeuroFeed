from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.GenerateStudyPlanView.as_view(), name='generate-plan'),
    path('user/<int:user_id>/', views.GetStudyPlansView.as_view(), name='user-plans'),
]