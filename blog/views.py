# Create your views here.
from django.http import HttpResponse
#from xsxsblog.blog.views import hello

def hello(request):
	return HttpResponse('hello world!!!!!!!!!!!')
