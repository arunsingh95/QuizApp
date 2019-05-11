# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Question(models.Model):
	question = models.CharField(max_length=200)
	question_seq_number = models.IntegerField()

	def __str__(self):
		return self.question

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice  =  models.CharField(max_length=200)
	is_right_answer = models.BooleanField(default=False)

	def __str__(self):
		return self.question.question + '  - '  + self.choice