from django.shortcuts import render, redirect
from .models import Licence, LicenceType
from .forms import CreateLicence
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
@login_required
def home(request):
    licences = Licence.objects.all().order_by('id')
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
        upload = update_created_by_and_last_updated_by(upload, request.user.email, request.user.email)       
        if upload.is_valid():
            upload.save()
            return redirect('home')
        else:
            return display_error(request, upload.errors)
    else:
        return render(request, 'licence/upload_licence.html', {'upload_licence': upload})

@login_required
def update_licence(request, licence_id):
    licence_id = int(licence_id)
    try:
        licence = Licence.objects.get(id = licence_id)
    except Licence.DoesNotExist:
        return redirect('home')
    # Get the old created by - making sure we don't overwrite the value
    created_by = Licence.objects.filter(id = licence_id).values('created_by')[0]['created_by']
    updated_licence = CreateLicence(request.POST or None, instance= licence)
    if request.method == 'POST':
        updated_licence = update_created_by_and_last_updated_by(updated_licence, created_by, request.user.email)
        if updated_licence.is_valid():
            updated_licence.save()
            return redirect('home')
        else:
            return display_error(request, updated_licence.errors)
    else:
        return render(request, 'licence/upload_licence.html', {'upload_licence': updated_licence})

@user_passes_test(lambda u: u.is_superuser)
def delete_licence(request, licence_id):
    licence_id = int(licence_id)
    try:
        licence = Licence.objects.get(id = licence_id)
    except Licence.DoesNotExist:
        return redirect('home')
    licence.delete()
    return redirect(home)

def display_error(request, error):
    messages.error(request, f'Something went wrong, please read the following message and try again. {error}')
    # Refresh current page
    return redirect(request.path_info)

def update_created_by_and_last_updated_by(licence, created_by, last_updated_by):
    licence.data._mutable = True
    licence.data['created_by'] = created_by
    licence.data['last_updated_by'] = last_updated_by
    licence.data._mutable = False
    return licence