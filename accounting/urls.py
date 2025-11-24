from django.urls import path

from . import views


urlpatterns = [
    path("", views.balance, name="balance"),
    # path("", views.AddKharj.as_view(), name="add"),
]
