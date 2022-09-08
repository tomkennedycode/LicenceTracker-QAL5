from django.shortcuts import render, redirect
from .models import Licence
from .forms import CreateLicence
from django.http import HttpResponse

# Create your views here.
def index(request):
    shelf = Licence.objects.all
    return render(request, 'licence/licence.html', {'shelf': shelf})

def upload(request):
    upload = CreateLicence()
    if request.method == 'POST':
        upload = CreateLicence(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse(""" Something went wrong, please reload the webpage by clicking <a href="{{url:'index'}}>Reload</a>" """)
    else:
        return render(request, 'licence/upload_licence.html', {'upload_licence': upload})

def update_licence(request, licence_id):
    licence_id = int(licence_id)
    try:
        licence_shelf = Licence.objects.get(id = licence_id)
    except Licence.DoesNotExist:
        return redirect('index')
    licence_form = CreateLicence(request.POST or None, instance= licence_shelf)
    if licence_form.is_valid():
        licence_form.save()
        return redirect('index')
    return render(request, 'licence/upload_licence.html', {'upload_licence': licence_form})

def delete_licence(request, licence_id):
    licence_id = int(licence_id)
    try:
        licence_shelf = Licence.objects.get(id = licence_id)
    except Licence.DoesNotExist:
        return redirect('index')
    licence_shelf.delete()
    return redirect(index)