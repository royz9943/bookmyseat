from django.http import HttpResponse


def index(request):
    return HttpResponse("Home")

def facebook(request):
    return HttpResponse('''<a href="https://www.facebook.com/">Facebook</a>''')