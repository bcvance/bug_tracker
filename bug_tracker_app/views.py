from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'bug_tracker_app/index.html')