from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("category/<int:category_id>/", views.category_items, name="category"),
    path("contact/", views.contact, name="contact"),
    path("signup/", views.signup, name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="core/login.html", authentication_form=LoginForm
        ),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
