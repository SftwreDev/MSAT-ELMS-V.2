from django.shortcuts import render, redirect


from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from quiz.decorators import student_required, teacher_required
from .models import Announcements
from .forms import CreateAnnouncementsForm


@method_decorator([login_required, student_required], name='dispatch')
class AnnouncementsList(ListView):
    model = Announcements
    template_name = 'announcements/announcements_board.html'
    context_object_name = 'announcements'

@method_decorator([login_required, teacher_required], name='dispatch')
class CreateAnnouncements(CreateView):
    model = Announcements
    template_name = 'announcements/create_announcement.html'
    form_class = CreateAnnouncementsForm
    context_object_name = 'create-announcements'


    def form_valid(self, form):
        announcements = form.save(commit=False)
        announcements.save()
        return redirect('home')
    
