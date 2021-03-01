from django.shortcuts import render
from django.contrib import messages
from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm


# Create your views here.
def newsletter_signup(request):
    err = False
    msg = ''
    if request.method == 'POST':
        form = NewsletterUserSignUpForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if NewsletterUser.objects.filter(email=instance.email).exists():
                msg = "Sorry! This email already exists."
                err = True
                # messages.error(request, msg) # it is not shown properly as an error message
            else:
                instance.save()
                messages.success(request, 'Subscription created successfully!')
    else:
        form = NewsletterUserSignUpForm()

    context = {
        'form': form,
        'err': err,
        'msg': msg
    }
    template = 'newsletter/newsletter_signup.html'
    return render(request, template, context)


def newsletter_unsubscribe(request):
    if request.method == 'POST':
        form = NewsletterUserSignUpForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if NewsletterUser.objects.filter(email=instance.email).exists():
                NewsletterUser.objects.filter(email=instance.email).delete()
                messages.success(request, f"You've been successfully unsubscribed!")
            else:
                messages.warning(request, f'Your email is not in the subscription email list!')
    else:
        form = NewsletterUserSignUpForm()

    context = {
        'form': form,
    }
    template = 'newsletter/newsletter_unsubscribe.html'
    return render(request, template, context)