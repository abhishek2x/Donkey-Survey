# forms/views.py
from allauth.account.utils import send_email_confirmation
from django.contrib.auth import decorators
from django.http import response
from django.template.defaultfilters import title
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from allauth.account.decorators import verified_email_required
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from forms.models import *

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, "home.html")

@verified_email_required
def dashboard(request):
    User = get_user_model()
    u = User.objects.get(username=request.user.username)
    formsCreated = Form.objects.filter(created_by=request.user)

    context = {
        'formsCreated': formsCreated,
        'count': formsCreated.count
    }

    return render(request, "dashboard.html", context)

@verified_email_required
def formdetail(request, pk):
    form = Form.objects.filter(id=pk)[0]
    questions = Question.objects.filter(form=pk)
    responses = Response.objects.filter(form_answered=pk)

    responseCount=0
    if questions.count():
        responseCount = int(responses.count() / questions.count())

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
    
    return render(request, "FormPages/form-detail.html", context)


def formsubmit(request, pk):
        
    form = Form.objects.filter(id=pk)[0]
    questions = Question.objects.filter(form=pk)

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
            instance = Response.objects.create(
                answered_by=answered_by,
                answered_by_email_id=answered_by_email_id,
                response=response,
                question_answered=question_answered,
                form_answered=form_answered
            )
            instance.save()
            print("Response for question saved")
            # send_mail(
            #     'You have successfully submitted the form',
            #     'You have successfully submitted the form, Thankyou for staying with SurveyDonkey.',
            #     'vitbook.smtp.team@gmail.com',
            #     [answered_by_email_id],
            #     fail_silently=True
            # )
        return redirect('formresults', form.id)


def formresults(request, pk):
    form = Form.objects.filter(id=pk)[0]
    questions = Question.objects.filter(form=pk)
    responses = Response.objects.filter(form_answered=pk)

    context = {
        'form': form,
        'questions': questions,
        'responses': responses,
    }

    return render(request, 'FormPages/form-result.html', context)


@verified_email_required
def formcreate1(request): 
    if request.method == 'POST':
        question_count = request.POST['question_count']
        request.session['question_count_value'] = question_count
        return redirect('formcreate2')

    return render(request, 'FormPages/form-create1.html')


@verified_email_required
def formcreate2(request):
    question_count = int(request.session.get('question_count_value'))
    context = {
        'n' : range(question_count)
        }
    
    if request.method == 'POST':
        
        # Create a new form
        formTitle = request.POST['form-title']
        formDescription = request.POST['form-description']
        form_instance = Form.objects.create(
            title=formTitle,
            description=formDescription,
            created_by=request.user
        )


        # Add Question Objects
        for i in range(question_count):
            ques = request.POST[str(i+1)]
            print(ques)
            ques_instance = Question.objects.create(
                question=ques,
                form=form_instance,
                created_by=request.user
            )

        # Saving both instances
        form_instance.save()
        ques_instance.save()

        # send_mail(
        #     'You have successfully created the form',
        #     'You have successfully created the form, Thankyou for staying with SurveyDonkey.',
        #     'vitbook.smtp.team@gmail.com',
        #     [request.user],
        #     fail_silently=True
        # )
        print("Form and All question saved")

        return redirect('dashboard')
    
    return render(request, 'FormPages/form-create2.html', context)

def deleteform(request, pk):
    instance = Form.objects.get(id=pk)
    instance.delete()

    # send_mail(
    #     'You form has been deleted',
    #     'You form has been deleted, Thankyou for staying with SurveyDonkey.',
    #     'vitbook.smtp.team@gmail.com',
    #     [request.user],
    #     fail_silently=True
    # )
    
    return redirect('dashboard')
