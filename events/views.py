from django.shortcuts import render


#-------------------- home -----------------#
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'home.html')

#-------------------- card ------------------#

def card(request):
    return render(request, 'card.html')

#-------------------- contact ---------------#

def contact(request):
    return render(request, 'contact.html')