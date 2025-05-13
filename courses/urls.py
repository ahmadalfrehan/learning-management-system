from django.urls import path
from . import views

urlpatterns = [
    path('', views.instructor_course_list, name='instructor_course_list'),
    path('create/', views.create_course, name='create_course'),
    path('<int:course_id>/edit/', views.update_course, name='update_course'),
    path('<int:course_id>/delete/', views.delete_course, name='delete_course'),



    # Modules
    path('<int:course_id>/modules/add/', views.add_module, name='add_module'),
    path('modules/<int:module_id>/edit/', views.edit_module, name='edit_module'),
    path('modules/<int:module_id>/delete/', views.delete_module, name='delete_module'),

    # Lessons
    path('modules/<int:module_id>/lessons/add/', views.add_lesson, name='add_lesson'),
    path('lessons/<int:lesson_id>/edit/', views.edit_lesson, name='edit_lesson'),
    path('lessons/<int:lesson_id>/delete/', views.delete_lesson, name='delete_lesson'),
]
