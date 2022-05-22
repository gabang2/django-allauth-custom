from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def hello(request):
    return render(request, template_name='login.html', context={})
