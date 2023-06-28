from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='storyposts'),
    path('story/create', views.create_story, name='create-story'),
    path("story/edit/<int:id>/", views.edit_story, name='edit-story'),
    path("story/delete/<int:id>/", views.delete_story, name='delete-story'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact')
]
