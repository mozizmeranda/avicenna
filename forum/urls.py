from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.DiseasePostView.as_view(({'get': 'list'}))),
    path('post/<int:pk>/', views.DiseasePostEditView.as_view()),
    path('post/comment/<int:pk>/', views.CommentsView.as_view()),
    path('post/comment/', views.CommentsView.as_view())

]
