from django.shortcuts import render

# Create your views here.
def reg(request):

    return render(request,"regpage.html")

def note(request):
    return(request,"notesvisual.html")