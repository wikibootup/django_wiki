from django.shortcuts import render
from django.http import HttpResponse

from polls.models import Poll

# Create your views here.
def index(request):
	all_list = Poll.objects.all()
	return render(request, "polls/index.html", {"all_list": all_list})

def detail(request, poll_id):
	return HttpResponse("hello this is detail page for" + poll_id)
	
def result(request, poll_id):
	return HttpResponse("hello this is result page for")
