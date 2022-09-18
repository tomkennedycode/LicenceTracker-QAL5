from django.shortcuts import render, redirect
from .models import Licence, LicenceType
from .forms import CreateLicence
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    licences = Licence.objects.all()
    # If user is superuser, show the delete button
    is_superuser = request.user.is_superuser
    for item in licences:
        item.licence_name = LicenceType.objects.get(id = item.licence_type_id)

    return render(request, 'licence/licence.html', {'licences': licences, 'is_superuser': is_superuser})

@login_required
def upload(request):
    upload = CreateLicence()
    if request.method == 'POST':
        upload = CreateLicence(request.POST, request.FILES)
        # Add created_by into DB from the user object
        upload.data._mutable = True
        upload.data['created_by'] = request.user.email
        upload.data['last_updated_by'] = request.user.email
        upload.data._mutable = False        
        if upload.is_valid():
            upload.save()
            return redirect('home')
        else:
            return HttpResponse(""" Something went wrong, please reload the webpage by clicking <a href="{{url:'home'}}>Reload</a>" """)
    else:
        return render(request, 'licence/upload_licence.html', {'upload_licence': upload})

@login_required
def update_licence(request, licence_id):
    licence_id = int(licence_id)
    try:
        licence = Licence.objects.get(id = licence_id)
    except Licence.DoesNotExist:
        return redirect('home')
    #Get the old created by - making sure we don't overwrite the value
    created_by = Licence.objects.filter(id = licence_id).values('created_by')[0]['created_by']
    updated_licence = CreateLicence(request.POST or None, instance= licence)
    updated_licence.data._mutable = True
    updated_licence.data['created_by'] = created_by
    updated_licence.data['last_updated_by'] = request.user.email
    updated_licence.data._mutable = False
    if updated_licence.is_valid():
        updated_licence.save()
        return redirect('home')
    return render(request, 'licence/upload_licence.html', {'upload_licence': updated_licence})

@login_required
def delete_licence(licence_id):
    licence_id = int(licence_id)
    try:
        licence = Licence.objects.get(id = licence_id)
    except Licence.DoesNotExist:
        return redirect('home')
    licence.delete()
    return redirect(home)