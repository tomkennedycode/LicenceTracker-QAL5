from django.shortcuts import render, redirect
from .models import Licence, LicenceType
from .forms import CreateLicence
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    shelf = Licence.objects.all()
    is_superuser = request.user.is_superuser
    for item in shelf:
        item.licence_name = LicenceType.objects.get(id = item.licence_type_id)

    return render(request, 'licence/licence.html', {'shelf': shelf, 'is_superuser': is_superuser})

@login_required
def upload(request):
    upload = CreateLicence()
    if request.method == 'POST':
        upload = CreateLicence(request.POST, request.FILES)
        upload.data._mutable = True
        upload.data['created_by'] = request.user.email
        upload.data['last_updated_by'] = request.user.email
        upload.data._mutable = False
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
    created_by = Licence.objects.filter(id = licence_id).values('created_by')[0]['created_by']
    licence_form = CreateLicence(request.POST or None, instance= licence_shelf)
    licence_form.data._mutable = True
    licence_form.data['created_by'] = created_by
    licence_form.data['last_updated_by'] = request.user.email
    licence_form.data._mutable = False
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