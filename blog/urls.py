from django.urls import path

from . import views

urlpatterns = [
    path('', views.starting_page, name='starting-page'),
    path('posts', views.posts, name='posts-page'),
    # slug transformer --> Matches any slug string consisting of ASCII letters or numbers, plus the hyphen and underscore characters
    path('posts/<slug:slug>', views.post_detail, name='post-details-page')
]
