from django.db import models


# Create your models here.


class Quizs(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class QuesModel(models.Model):
    question = models.CharField(max_length=200, null=True)
    quiz_name = models.ForeignKey(Quizs, on_delete=models.CASCADE)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    op3 = models.CharField(max_length=200, null=True)
    op4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.question