from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Welcome to the best website ever</h1>')