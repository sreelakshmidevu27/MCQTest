from django.db import models

# class QuizCategory(models.Model):
#     title=models.CharField(max_length=100)
    

#     class Meta:
#         verbose_name_plural='Categories'

#     def __str__(self):
#         return self.title
    
class QuizQuestion(models.Model):
    #category=models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    question=models.TextField()
    opt_1=models.CharField(max_length=200)
    opt_2=models.CharField(max_length=200)
    opt_3=models.CharField(max_length=200)
    opt_4=models.CharField(max_length=200)
    time_limit=models.IntegerField()
    right_opt=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Questions'

    def __str__(self):
        return self.question
