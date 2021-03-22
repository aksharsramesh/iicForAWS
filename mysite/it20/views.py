from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core.files.storage import FileSystemStorage
from .forms import SignupForm, NEWIdeaSubmissionForm
from .tokens import account_activation_token
from .models import newIdea

def it20about(request):
    return render(request, 'it20/it20about.html')

def postsignup(request):
    return render(request, 'it20/post-signup.html')

def contact_view(request):
    return render(request, 'it20/contact_page.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            current_site = get_current_site(request)
            """
            mail_subject = 'Activation Link For Ideathon2020'
            message = render_to_string('it20/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            """
            return render(request, 'it20/post-signup.html')
    else:
        form = SignupForm()
    return render(request, 'it20/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('it20:it20about')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def downloadALL_view(request):
    ideas = newIdea.objects.all().order_by('date')
    return render(request, 'it20/download_page.html', { 'ideas':ideas })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('it20:it20about')
    else:
        form = AuthenticationForm()
    return render(request, 'it20/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('it20:it20about')

@login_required(login_url='it20:login')
def submit(request):
    if request.method == 'POST':
            form = NEWIdeaSubmissionForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                #return HttpResponse('Your Response Has Been Recorded. Return To http://iicjssstu.in/it20')
                return render(request, 'it20/AfterideaSubPage.html')
    else:
        form = NEWIdeaSubmissionForm()
        return render(request, 'it20/ideaSubPage.html', {'form':form})

def download_view(request):
    fs = FileSystemStorage()
    filename = 'ideaFormat/Ideathon_2.0.docx'
    if fs.exists(filename):
        with fs.open(filename) as DemoDocument:
            response = HttpResponse(DemoDocument, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename="Ideathon_2.0.docx"'
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')
