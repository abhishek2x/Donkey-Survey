from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models


class Form(models.Model):
    
    """
    Store Forms that will be created/submitted by the users.
    :model:`forms.Form`.
    """


    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(to=User, on_delete=CASCADE, default=1)

    def __str__(self):
        return self.title + ": " + self.description

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.title

class Question(models.Model):

    """
    Store Questions of all the Forms.
    :model:`forms.Question`.
    """

    question = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    form = models.ForeignKey(to=Form, on_delete=CASCADE)
    created_by = models.ForeignKey(to=User, on_delete=CASCADE)

    def __str__(self):
        return  self.form.title + ": " + self.question


class Response(models.Model):

    """
    Store Responses of all the Questions of all the Forms.
    :model:`forms.Response`.
    """

    answered_by = models.CharField(max_length=255)
    response = models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    answered_by_email_id = models.EmailField(max_length=255)
    question_answered = models.ForeignKey(to=Question, on_delete=CASCADE, related_name="voted_on")
    form_answered = models.ForeignKey(to=Form, on_delete=CASCADE, related_name="voted_on")

    def __str__(self):
        return self.form_answered.title + ": "+ self.question_answered.question
