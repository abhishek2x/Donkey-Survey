# config/views.py
from django.http import response
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
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


# @login_required
# def formdetail(request):
#     if request.method == 'POST':
#         form = CreatePollForm(request.POST)
#         if form.is_valid():
#             form.save()
#             send_mail(
#                 'Your Poll is Successfully Created',
#                 'Your Poll has been Created Successfully, You may check it by following the Link.',
#                 'vitbook.smtp.team@gmail.com',
#                 [request.user.email],
#                 fail_silently=False
#             )
#             return redirect('poll_home')
#     else:
#         form = CreatePollForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'social/poll_create.html', context)
    
def formsubmit(request, pk):
    if request.method == 'GET':
        context = {}
        return render(request, 'FormPages/form-submit.html', context)