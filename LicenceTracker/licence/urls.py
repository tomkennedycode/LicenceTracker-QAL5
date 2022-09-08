from django.urls import path
from . import views
from LicenceTracker.settings import DEBUG, STATIC_ROOT, STATIC_URL, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload-licence'),
    path('update/<int:licence_id>', views.update_licence),
    path('delete/<int:licence_id>', views.delete_licence)
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)