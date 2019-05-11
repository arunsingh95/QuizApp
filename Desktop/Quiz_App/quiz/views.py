# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render ,redirect
from django.http import HttpResponse
from quiz.models import  Question,Choice
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.urls import reverse

# This is the first page that user encounters 
def first_view(request):
	#count give the total number of registered user 
	count = User.objects.count()
	return render(request,'start.html',{'count':count})

# This is the signup page function 
def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('quiz:first_view')
	else:
		form = UserCreationForm()		
	return render(request,'registration/signup.html',{'form':form})	

def  questions_list(request, *args, **kwargs):
	if request.method == 'GET':
		context = {}
		context['question_no'] = kwargs.get('id')
		question = Question.objects.filter(question_seq_number=kwargs.get('id'))
		if len(question) == 1:
			question = question[0]
			context['question'] = question
			return render(request,'base.html', context)	
		else:
				return redirect(reverse('quiz:results'))

	elif request.method == 'POST':
		question_no = request.POST.get('question_no')
		if question_no == '1':
			request.session['right_answer_count'] = 0
		question_no = int(question_no) + 1
		choice_id = request.POST.get('choice')
		choice_list = Choice.objects.filter(id=choice_id, is_right_answer=True)
		if len(choice_list) == 1:
			request.session['right_answer_count']  += 1
		return redirect(reverse('quiz:questions_list', kwargs={ 'id' : str(question_no)}))

#returns selected choice from the user to check whether its correct or not
def timer(request):
	return render(request,'timerComp.html')	

def Result(request):
	return render(request, 'home.html')

# def detail(request):
# 	questions_list = Question.objects.all().order_by('id')
# 	ques_id = list(questions_list.values_list('id', flat=True))
# 	print 'ques_id',ques_id
# 	for val in ques_id:
# 		print 'EEE',val
# 		return HttpResponse("You're looking at question %s." % val)	
