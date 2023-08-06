from django.shortcuts import render

# Create your views here.
def list_todo(request):
    #logic
    return render(request,"index.html")