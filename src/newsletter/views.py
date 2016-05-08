from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import SignUpForm, ContactForm
# Create your views here.


def home(request):
    title = "Welcome, %s" % request.user
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        # print(request.POST['email'])
        instance = form.save(commit=False)
        print(instance.fullName)
        if not instance.fullName:
            instance.fullName = "Justin"
        instance.save()
        context = {
            "title": "Thanks"
        }

    return render(request, "home.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_fullName = form.cleaned_data.get('fullName')
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        # print(fullName, email, message)
        # print(form.cleaned_data)
        subject = "Site Contact Form"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, form_email]
        contact_message = "%s: %s via %s" % (
            form_fullName,
            form_message,
            from_email
        )

        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)

    context = {
        "form": form
    }

    return render(request, "form.html", context)
