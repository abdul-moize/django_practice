from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    # ex: /users/
    path("", views.index, name="index"),
    # ex: /users/5/
    path("<int:question_id>/", views.detail, name="details"),
    # ex: /users/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /users/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # ex: /users/add_user
    path("add_user/", views.add_user, name="add_user"),
]
