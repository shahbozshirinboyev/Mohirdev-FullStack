from django.urls import path
from .views import CreateUserView, VerifyAPIView, GetNewVerification, \
    ChangeUserInformationView, ChangeUserPhotoView, LoginView, \
    TokenRefreshView, LogoutView, ForgotPasswordView, ResetPasswordView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('signup/', CreateUserView.as_view()),
    path('verify/', VerifyAPIView.as_view()),
    path('new-verify/', GetNewVerification.as_view()),
    path('change-user/', ChangeUserInformationView.as_view()),
    path('change-user-photo/', ChangeUserPhotoView.as_view()),
    path('forgot-password/', ForgotPasswordView.as_view()),
    path('reset-password/', ResetPasswordView.as_view()),
]