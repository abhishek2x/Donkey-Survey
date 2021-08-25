# config/views.py
from django.db.models.query_utils import Q
from django.http import response
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from forms.models import *

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

@login_required
def dashboard(request):
    User = get_user_model()
    u = User.objects.get(username=request.user.username)
    print("User Logged In :", u)

    formsCreated = Form.objects.filter(created_by=request.user)
    print(formsCreated)
    return render(request, "dashboard.html", {'formsCreated': formsCreated})



@login_required
def formdetail(request, pk):
    form = Form.objects.filter(id=pk)[0]
    questions = Question.objects.filter(form=pk)
    responses = Response.objects.filter(form_answered=pk)

    responseCount = responses.count()

    # print(form)
    # print(questions)       
    print(responses)            
    print(responseCount)            

    context = {
        'form': form,
        'questions': questions,
        'responses': responses,
        'responseCount': responseCount
    }
    
    return render(request, "FormPages/detail.html", context)


def formsubmit(request, pk):
        
    form = Form.objects.filter(id=pk)[0]
    questions = Question.objects.filter(form=pk)
    for q in questions: 
        print(q.id)

    if request.method == 'GET':
        context = {
            'form': form,
            'questions': questions
            }
        return render(request, 'FormPages/form-submit.html', context)

        # print(request.POST['answered_by_email_id'])

    if request.method == 'POST':
        print("FORM SUBMITTED")
        
        answered_by = request.POST['answered_by']
        answered_by_email_id = request.POST['answered_by_email_id']
        form_answered = form

        for ques in questions:
            response = request.POST[str(ques.id)]
            question_answered = ques
            
            # Create a new Object for Response Model
            Response.objects.create(
                answered_by=answered_by,
                answered_by_email_id=answered_by_email_id,
                response=response,
                question_answered=question_answered,
                form_answered=form_answered
            )
            print("Response for question saved")
        return redirect('formresults', form.id)


def formresults(request, pk):
    context = {}
    return render(request, 'FormPages/form-result.html', context)
