from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.getAllJobs, name='jobs'),
    path('jobs/<str:id>/', views.getJobById, name='job'),
    path('jobs/new/', views.createJob, name='new_job'),
    path('jobs/<str:id>/update/', views.updateJob, name='update_job'),
]
