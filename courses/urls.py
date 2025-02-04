from django.urls import path
from . import views


app_name = 'courses'


urlpatterns = [
    path('list/', views.course_list, name='list'),
    path('add/', views.add_course, name='add'),
    path(
        "courses/course/<int:year>/<int:month>/<int:day>/<slug:slug>/",
        views.course_detail,
        name="detail",
    ),
    path('delete/<int:pk>/', views.course_delete, name='delete'),
]
