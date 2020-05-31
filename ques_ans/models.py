from django.db import models

# Create your models here.

class Quiz(models.Model):
	title = models.CharField(max_length=500)
	total_questions = models.IntegerField(default=0)
	description = models.CharField(max_length=1000)
	is_available = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	def get_questions_list(self):
		return self.question_set.all()

class Question(models.Model):
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questios", null=True)
	title = models.CharField(max_length=300)
	order = models.IntegerField(default=0)

	def __str__(self):
		return self.title
	def get_answers_list(self):
		return self.answer_set.all()

class Answer(models.Model):
	title = models.CharField(max_length=300)
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
	is_correct = models.BooleanField(default=False)

	def __str__(self):
		return self.question.title +" "+ self.title