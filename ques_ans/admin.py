from django.contrib import admin
from .models import Quiz, Question, Answer
# Register your models here.
quiz_models = [Quiz, Question, Answer]

admin.site.register(quiz_models)