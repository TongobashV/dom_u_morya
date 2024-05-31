from django.shortcuts import render


# Create your views here.
def houses_list(request):
    return render(request, "houses/houses_list.html")

