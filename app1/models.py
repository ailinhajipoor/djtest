from django.db import models
class Question(models.Model):
    text =models.CharField(max_length=300)
    pub_date =models.DateTimeField


class Answer(models.Model):
    pass