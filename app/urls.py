from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('app/<int:user_id>/', views.show_user_info),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('aboutus/clubs/', views.clubs, name='clubs'),
    path('aboutus/depts/', views.depts, name='depts'),
    path('aboutus/techassoc/', views.techassoc, name='techassoc'),
    path('aboutus/ngos/', views.ngos, name='ngos'),
    path('complaints/',views.complaints, name='complaints'),
    path('submit_complaint',views.submit_complaint, name='submit-complaint'),
    path('calendar/', views.calendar, name='calendar'),
    path('clubs/', views.clubs, name='clubs'),
    path('logout/', views.logout_view, name='logout'),
]
