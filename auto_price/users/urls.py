from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from users import views
from users.forms import UserPasswordChangeForm


app_name = "users"


urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.registration, name="registration"),
    path("profile/", views.profile, name="profile"),
    path("profile/<slug:username>/", views.profile, name="profile_other_user"),


    path("password-change", PasswordChangeView.as_view(
        form_class=UserPasswordChangeForm,
        template_name='users/password_change_form.html',
        success_url = reverse_lazy("users:password_change_done")
    ), name="password_change"),
    path("password-change/done", PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'
    ), name="password_change_done"),


    path(
        "password-reset",
        PasswordResetView.as_view(
            template_name="users/password_reset_form.html",
            email_template_name="users/password_reset_email.html",
            success_url=reverse_lazy("users:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            success_url=reverse_lazy("users:password_reset_complite"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/complite/",
        PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complite.html"
        ),
        name="password_reset_complite",
    ),
]
