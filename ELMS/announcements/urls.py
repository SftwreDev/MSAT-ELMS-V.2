from django.urls import path

from . import views

app_name = 'announcements'
urlpatterns = [
    path('announcements/', views.AnnouncementsList.as_view(), name='list-of-announcements'),
    path('announcementts/create-announcements/', views.CreateAnnouncements.as_view(), name='create-announcements'),
]
