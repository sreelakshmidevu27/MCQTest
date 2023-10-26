from rest_framework import serializers
from .models import QuizQuestion

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = ['question','opt_1','opt_1','opt_1','opt_1','time_limit','right_opt']


