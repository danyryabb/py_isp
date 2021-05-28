# from django.db import models
#
# PRIORITY = [
#     ("L", "Low"),
#     ("M", "Medium"),
#     ("H", "High"),
# ]
#
# # Create your models here.
# class Question(models.Model):
#     title = models.CharField(max_length=50)
#     question = models.TextField(max_length=200)
#     priority = models.CharField(max_length=1, choices=PRIORITY)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = "The Question"
#         verbose_name_plural = "Peoples questions"