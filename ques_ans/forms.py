from django import forms
from django.forms.widgets import RadioSelect
from .models import Quiz, Question, Answer



class QuestionForm(forms.Form):
	def __init__(self, question, *args, **kwargs):
		super(QuestionForm, self).__init__(*args, **kwargs)
		choice_list = [q for q in question.get_answers_list() ]
		self.fields["answers"] = forms.ChoiceField(choices=choice_list, widget=RadioSelect)

	# answers = forms.ModelChoiceField(queryser=Answer.objects.filter())
	# class Meta:
	# 	model = Question
	# 	fields = "__all__"