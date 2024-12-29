from django.urls import path
from . import views


app_name = 'courses'


urlpatterns = [
    path('list/', views.course_list, name='list'),
    path('add/', views.add_course, name='add'),
    path(
        'course/<int:year>/<int:month>/<int:day>/<slug:slug>/',
        views.course_detail,
        name='course_detail'
    ),
    path('delete/<int:pk>/', views.course_delete, name='delete'),
    path('course/delete/<int:pk>/', views.course_delete, name='course_delete')
]
