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
                print(msg)
                err = True
                # messages.error(request, msg) # it is not shown properly as an error message
            else:
                instance.save()
                messages.success(request, f'Subscription created successfully!')
    else:
        form = NewsletterUserSignUpForm()

    context = {
        'form': form,
        'err': err,
        'msg': msg
    }
    template = 'newsletter/newsletter_signup.html'
    return render(request, template, context)


