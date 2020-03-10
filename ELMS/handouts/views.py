from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView

from django.urls import reverse_lazy

from .models import Handouts
from .forms import HandoutsForm
from .filters import HandoutsSearch
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from quiz.decorators import student_required, teacher_required

class ListofHandouts(ListView):
    model = Handouts
    template_name = 'handouts/list_of_handouts.html'
    context_object_name = 'list_of_handouts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = HandoutsSearch(self.request.GET, queryset=self.get_queryset())
        return context


@method_decorator([login_required, teacher_required], name='dispatch')
class UploadHandouts(CreateView):
    model = Handouts
    template_name = 'handouts/upload_handouts.html'
    context_object_name = 'handouts'
    form_class = HandoutsForm
    success_url = reverse_lazy("handouts:list-of-handouts")

@method_decorator([login_required, teacher_required], name='dispatch')
class FileDeleteView(DeleteView):
    model = Handouts
    context_object_name = 'file'
    template_name = 'handouts/confirm_delete.html'
    success_url = reverse_lazy('handouts:list-of-handouts')
    





