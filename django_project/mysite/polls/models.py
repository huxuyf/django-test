from django.db import models
from django.utils import timezone
from django.forms import ModelForm

class Question(models.Model):
    question_text = models.CharField('问题',max_length=100)
    pub_date = models.DateTimeField('发布时间')

    def __str__(self):
        return self.question_text
    def __unicode__(self):
        return "123"
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField('投票选项',max_length=100)
    votes = models.IntegerField('票数',default=0)

    def __str__(self):
        return self.choice_text 
    

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'