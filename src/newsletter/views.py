from django.shortcuts import render

from .forms import SignUpForm
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
