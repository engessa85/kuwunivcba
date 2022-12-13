
from django.urls import path
from . import views
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path("", views.login_page, name="login_page"),
    path('logout/', views.logout_page, name='logout_page'),
    path("signup/", views.signup_page, name="signup_page"),
    path("teacher/", views.teacher_page, name="teacher_page"),
    path('faculty/', views.faculty_page, name='faculty_page'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    path('summary/', views.summary_page, name='summary_page'),
    path('email/', views.email_page, name='email_page'),
    path('modify-teacher/<str:pk>', views.teacher_modify_page, name='teacher_modify_page'),

    path('course/', views.course_page, name='course_page'),
    path('add-course/', views.add_course_page, name='add_course_page'),
    path('modify-course/<str:pk>', views.modify_course_page, name='modify_course_page'),
    path('delete-course/<str:pk>', views.delete_course_page, name='delete_course_page'),

    path('time/', views.time_page, name='time_page'),
    path('summary-admin/<str:pk>', views.summary_page_for_admin, name='summary_page_for_admin'),
    path('modify-teacher-admin/<str:pk>', views.teacher_modify_page_for_admin, name='teacher_modify_page_for_admin'),

    path('time-schedual/', views.schedual_time_page, name='schedual_time_page'),
    path('add-time-schedual/', views.add_schedual_time_page, name='add_schedual_time_page'),
    path('modify-time-schedual/<str:pk>', views.modify_schedual_time_page, name='modify_schedual_time_page'),
    path('delete-time-schedual/<str:pk>', views.delete_schedual_time_page, name='delete_schedual_time_page'),

    path('faculty-detail/', views.faculty_page_detail, name='faculty_page_detail'),
    path('faculty-modify/<str:pk>', views.faculty_page_modify, name='faculty_page_modify'),

    path('schedule/', views.schedule_course_page, name='schedule_course_page'),
    path('schedule-time/', views.schedule_time_page_, name='schedule_time_page_'),


    path('schedule-time-1/', views.schedule_time_page_1, name='schedule_time_page_1'),
    path('schedule-time-2/', views.schedule_time_page_2, name='schedule_time_page_2'),
    path('schedule-time-3/', views.schedule_time_page_3, name='schedule_time_page_3'),

    path('archive/', views.archive_page, name='archive_page'),
    path('archive-user/', views.archive_user_page, name='archive_user_page'),
    path('archive-user-summary/<str:pk>', views.archive_user_summary_page, name='archive_user_summary_page'),


    


    

    

]




