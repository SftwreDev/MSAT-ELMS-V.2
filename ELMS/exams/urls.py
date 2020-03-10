from django.urls import include, path

from exams import views

app_name = 'exams'
urlpatterns = [
    
    path('students/', views.StudentsExamsListView.as_view(), name='exams_list'),
    path('students/exams/<int:pk>/', views.take_exams, name='take_exams'),
    path('students/taken/', views.TakenExamsListView.as_view(), name='taken_exams_list'),
    path('teachers/create-exams/', views.ExamsCreateView.as_view(), name='create-new-exams'),
    path('teachers/list-of-exams/', views.TeachersExamsListView.as_view(), name='created_exams_list'),
    path('teachers/update-exams/<int:pk>/', views.ExamsUpdateView.as_view(), name = 'update_exams'),
    path('teachers/<int:pk>/delete-exams/', views.ExamsDeleteView.as_view(), name='exams_delete'),
    path('teachers/exams/<int:pk>/question/add/', views.exams_question_add, name='exams_question_add'),
    path('teachers/exams/<int:exams_pk>/question/<int:question_pk>/', views.question_change, name='exams_question_change'),
    #path('teachers/exams/<int:exams_pk>/question/<int:question_pk>/', views.question_change, name='question_change'),
    path('teachers/exams/<int:pk>/results/', views.ExamsResultsView.as_view(), name='exams_results'),
    path('teachers/exams/<int:exams_pk>/question/<int:question_pk>/delete/', views.QuestionDeleteView.as_view(), name='exams_question_delete'),

]
