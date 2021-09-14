from django.urls import path
from . import views


urlpatterns = [
    path('login',views.login),
    path('studentList',views.studentList),
    path('mentorList',views.mentorList),
    path('updateUser',views.updateUser),
    path('questionList',views.questionList),
    path('addQuestion',views.addQuestion),
    path('getAuditLog',views.getAuditLog),
    path('updateQuestion',views.updateQuestion),
    path('getSubmissions',views.getSubmissions),
    path('getPendingJudgeList',views.getPendingJudgeList),
    path('updateSubmission',views.updateSubmission)
]