from django.shortcuts import render
from constance import config
from django.http import Http404
from django.conf import settings
from .models import Message
from .forms import MessageForm
import requests

# Create your views here.

def index(request):
    GOOGLE_RECAPTCHA_SITE_KEY = config.GOOGLE_RECAPTCHA_SITE_KEY
    GOOGLE_RECAPTCHA_SECRET_SITE_KEY = config.GOOGLE_RECAPTCHA_SECRET_SITE_KEY
    settings = config
    context = {
    "config": settings
    }
    if request.method == 'POST':
        post_request = request.POST
        data = {
            "response": post_request.get("g-recaptcha-response"),
            "secret": GOOGLE_RECAPTCHA_SECRET_SITE_KEY,
        }
        resp = requests.post(
            "https://www.google.com/recaptcha/api/siteverify", data=data
        )
        result_json = resp.json()
        print("captcha response is : ", result_json)
        if not result_json.get("success"):
            robot_context = {"robot": True}
            context.update(robot_context)
        else:
            form = MessageForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, f"comming-soon/pages/success.html", context)
            # else:
            #     context["form"] = form
            #     return render(request, "darcos/contact.html", context)

    return render(request, f"comming-soon/pages/index.html", context)
