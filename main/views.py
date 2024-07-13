from django.shortcuts import render
from . import  models

def index(request):
    banner=models.Banner.objects.all()
    contacts=models.Contact.objects.all()
    our_serve=models.Our_Services.objects.all()
    technician=models.Technicians.objects.all()
    opening_hours=models.Opening_Hours.objects.all()
    newsletter=models.Newsletter.objects.all()
    adress=models.Address.objects.all()

    context={
        'banner':banner,
        'contacts':contacts,
        'our_serve':our_serve,
        'technician':technician,
        'opening_hours':opening_hours,
        'newsletter':newsletter,
        'adress':adress,
             }
    if request.method == 'POST':
        sing_up=request.POST['email']
        models.Newsletter.objects.create(
                  email=sing_up
            )
    
    return render(request , 'index.html', context)

