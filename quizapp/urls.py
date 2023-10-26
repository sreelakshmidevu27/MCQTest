from django.urls import path
from .views import QuestionListCreateView

urlpatterns = [
    path('api/questions/', QuestionListCreateView.as_view(), name='question-list'),
]
