from django.shortcuts import render, redirect
from .models import Licence, LicenceType
from .forms import CreateLicence
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    print('here p2')
    shelf = Licence.objects.all()
    for item in shelf:
        item.licence_name = LicenceType.objects.get(id = item.licence_type_id)

    return render(request, 'licence/licence.html', {'shelf': shelf})

@login_required
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

@login_required
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

@login_required
def delete_licence(request, licence_id):
    licence_id = int(licence_id)
    try:
        licence_shelf = Licence.objects.get(id = licence_id)
    except Licence.DoesNotExist:
        return redirect('index')
    licence_shelf.delete()
    return redirect(index)