from django.urls import path
from . import views


app_name = 'students'


urlpatterns = [
    path('list/', views.student_list, name='list'),
    path('add/', views.add_student, name='add'),
    path('<int:pk>/delete/', views.delete_student, name='delete'),
    path('student/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.student_detail, name='detail')
]