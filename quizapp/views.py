from django.shortcuts import render
from rest_framework import generics
from .models import QuizQuestion
from .serializers import QuestionSerializer

class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuestionSerializer

