from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, \
  PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from .views import UserLogin, DashboardView, UserRegister, SignUpView, edit_user, EditUserView

urlpatterns = [
  # path('login/', UserLogin, name='login'),
  path('login/', LoginView.as_view(), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
  path('password-change/', PasswordChangeView.as_view(), name='password_change'),
  path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
  path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
  path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
  path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
  path('password-reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
  path('profile/', DashboardView, name='profile'),
  path('profile/edit/', EditUserView.as_view(), name='edit_user_info'),
  path('signup/', UserRegister, name='signup' ),
]