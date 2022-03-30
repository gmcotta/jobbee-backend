from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.getAllJobs, name='jobs'),
    path('jobs/new/', views.createJob, name='new_job'),
    path('jobs/<str:id>/', views.getJobById, name='job'),
    path('jobs/<str:id>/update/', views.updateJob, name='update_job'),
    path('jobs/<str:id>/delete/', views.deleteJob, name='delete_job'),
    path('jobs/<str:jobId>/check/', views.isApplied, name='is_applied_to_job'),
    path('jobs/<str:jobId>/apply/', views.applyToJob, name='apply_to_job'),
    path('jobs/<str:jobId>/candidates/', views.getCandidatesApplied, name='get_candidates_applied'),
    path('me/jobs/applied/', views.getCurrentUserAppliedJobs, name='current_user_applied_jobs'),
    path('me/jobs/', views.getCurrentUserJobs, name='current_user_jobs'),
    path('stats/<str:topic>/', views.getTopicStats, name='get_topic_stats'),
]
