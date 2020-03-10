from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'handouts'
urlpatterns = [
    path('handouts/', views.ListofHandouts.as_view(), name='list-of-handouts'),
    path('handouts/upload-new-handouts/', views.UploadHandouts.as_view(), name='upload-handouts'),
    path('handouts-document/<int:pk>/delete/', views.FileDeleteView.as_view(), name='file_delete'),
    
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)