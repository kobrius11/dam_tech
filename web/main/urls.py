from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str>", views.FormView.as_view(), name="form_page"),
    path("success/", views.success_page, name="success_page"),

]