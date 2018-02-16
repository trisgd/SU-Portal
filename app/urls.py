from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('app/<int:user_id>/', views.show_user_info),
    path('contact/', views.contact, name='contact'),
    path('complaints/',views.complaints, name='complaints'),
    path('submit_complaint',views.submit_complaint, name='submit-complaint'),
    path('calendar/', views.calendar, name='calendar'),
    path('clubs/', views.clubs, name='clubs'),
]
