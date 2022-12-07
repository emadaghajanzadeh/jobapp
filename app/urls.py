from django.urls import path

from app.views import hello,job_detail, job_list


urlpatterns = [
    #here hello is function name
    # path('', job_list),
    #using reverse function
    path('', job_list, name = "jobs_home"),
    #<id> is the dynamic part here:
    # path('job/<id>', job_detail),
    #<id> type now is specified (string is default):
    # path('job/<int:id>', job_detail)
    # using reverse function:
    path('job/<int:id>', job_detail, name = 'jobs_detail'),

    # Path to url inside templates folder
    path('hello/', hello, name = "hello")


]