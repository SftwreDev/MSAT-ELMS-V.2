from django.shortcuts import render, redirect


from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import StudentProfile
from .forms import StudentProfileForm

from quiz.models import TakenQuiz, TakenExams
from .filters import StudentSearch
from django.urls import reverse, reverse_lazy

class StudentProfileView(TemplateView):

    template_name = 'profile/student_profile.html'


class StudentAboutProfileView(TemplateView):

    template_name = 'profile/student_about.html'
  


class StudentProfileCreate(CreateView):
    model = StudentProfile
    form_class = StudentProfileForm
    template_name = 'profile/student_create_profile.html'
    success_url = reverse_lazy('profile:student-profile')





class TakenQuizListProfileView(ListView):
    model = TakenQuiz
    context_object_name = 'taken_quizzes'
    template_name = 'profile/student_taken_quiz.html'

    def get_queryset(self):
        queryset = self.request.user.student.taken_quizzes \
            .select_related('quiz', 'quiz__year_level') \
            .order_by('quiz__name')
        return queryset


class TakenExamsListProfileView(ListView):
    model = TakenExams
    template_name = 'profile/students_taken_exams_profile.html'
    context_object_name = 'taken_exams'

    def get_queryset(self):
        queryset = self.request.user.student.taken_exams \
            .select_related('exams', 'exams__year_level') \
            .order_by('exams__name')
        return queryset


class StudentOptionProfileView(TemplateView):

    template_name = 'profile/student_option_profile.html'
  



class StudentProfileUpdateView(UpdateView):
    model = StudentProfile
    form_class = StudentProfileForm
    template_name = 'profile/student_update_profile.html'
    success_url = reverse_lazy('profile:student-profile')



    


class ListOfStudentView(ListView):
    model = StudentProfile
    context_object_name = 'students'
    template_name = 'teacherprofile/list_of_students.html'
    ordering = ['last_name',]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = StudentSearch(self.request.GET, queryset=self.get_queryset())
        return context




class ProfileUpdateView(UpdateView):
    model = StudentProfile
    context_object_name = 'student'
    form_class = StudentProfileForm
    template_name = 'profile/student_update_profile.html'
    success_url = reverse_lazy('profile:student-profile')
    

class ProfileDeleteView(DeleteView):
    model = StudentProfile
    template_name = 'profile/student_profile_delete.html'
    success_url = reverse_lazy('profile:student-profile')



   