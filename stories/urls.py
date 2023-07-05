from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='storyposts'),
    path('story/create', views.create_story, name='create-story'),
    path("story/edit/<int:id>/", views.edit_story, name='edit-story'),
    path("story/delete/<int:id>/", views.delete_story, name='delete-story'),
    path('comments/add/<int:id>/', views.create_comment, name='add-comment'),
    path("delete-comment/<int:id>/", views.delete_comment, name='delete-comment'),
    path("like-story/<int:id>", views.like_story, name='like-story'),
    path("unlike-story/<int:id>", views.unlike_story, name='unlike-story'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact')
]
