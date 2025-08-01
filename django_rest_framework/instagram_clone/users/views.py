from django.shortcuts import render
from .models import User, DONE, CODE_VERIFIED, NEW, VIA_EMAIL, VIA_PHONE
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from .serializers import SignUpSerializer, ChangeUserInformation, ChangeUserPhotoSerializer, \
     LoginSerializer, TokenRefreshSerializer, LogoutSerializer, ForgotPasswordSerializer, \
     ResetPasswordSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from rest_framework.exceptions import ValidationError
from shared.utility import send_email
from django.utils import timezone
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from shared.utility import check_email_or_phone
from rest_framework.permissions import AllowAny
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound

# Create your views here.
class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = SignUpSerializer

class VerifyAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        user = self.request.user
        code = self.request.data.get('code')

        self.check_verify(user, code)
        return Response(
            data = {
                'success': 'True',
                'auth_status': user.auth_status,
                'access': user.token()['access'],
                'refresh_token': user.token()['refresh_token'],
            }
        )

    @staticmethod
    def check_verify(user, code):
        verifies = user.verify_codes.filter(
            expiration_time__gte=timezone.now(),
            code=code,
            is_confirmed=False
        )
        if not verifies.exists():
            data = {
                'message': 'The verification code is incorrect or outdated.'
            }
            raise ValidationError(data)
        else:
            verifies.update(is_confirmed=True)
        if user.auth_status == NEW:
            user.auth_status = CODE_VERIFIED
            user.save()
        return True

class GetNewVerification(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        self.check_verification(user)
        if user.auth_type == VIA_EMAIL:
            code = user.create_verify_code(VIA_EMAIL)
            send_email(user.email, code)
        elif user.auth_type == VIA_PHONE:
            code = user.create_verify_code(VIA_PHONE)
            send_email(user.email, code)
        else:
            data = {
                "message": "Invalid email or phone number."
            }
            raise ValidationError(data)
        return Response(
            {
                'success': True,
                'message': 'Verification code resent.',
            }
        )


    @staticmethod
    def check_verification(user):
        verifies = user.verify_codes.filter(expiration_time__gte=timezone.now(), is_confirmed=False)
        if verifies.exists():
            data = {
                "message": "You have to wait to get a new code."
            }
            raise ValidationError(data)

# class ChangeUserInformationView(UpdateAPIView):
#     permission_classes = [IsAuthenticated, ]
#     serializer_class = ChangeUserInformation
#     http_method_names = ['patch', 'put']

#     def get_object(self):
#         return self.request.user

#     def update(self, request, *args, **kwargs):
#         super(ChangeUserInformation, self).update(request, *args, **kwargs)
#         data = {
#             'success': True,
#             'message': 'User update successfully.',
#             'auth_status': self.request.user.auth_status,
#         }
#         return Response(data, status=200)

#     def partial_update(self, request, *args, **kwargs):
#         super(ChangeUserInformation, self).update(request, *args, **kwargs)
#         data = {
#             'success': True,
#             'message': 'User update successfully.',
#             'auth_status': self.request.user.auth_status,
#         }
#         return Response(data, status=200)

class ChangeUserInformationView(UpdateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ChangeUserInformation  # Bu to'g'ri, serializer emas model serializer
    http_method_names = ['patch', 'put']

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        # ❌ noto'g'ri
        # super(ChangeUserInformation, self).update(request, *args, **kwargs)

        # ✅ to'g'ri
        response = super().update(request, *args, **kwargs)

        data = {
            'success': True,
            'message': 'User updated successfully.',
            'auth_status': self.request.user.auth_status,
        }
        return Response(data, status=200)

    def partial_update(self, request, *args, **kwargs):
        # ❌ noto'g'ri
        # super(ChangeUserInformation, self).update(request, *args, **kwargs)

        # ✅ to'g'ri
        response = super().partial_update(request, *args, **kwargs)

        data = {
            'success': True,
            'message': 'User updated successfully.',
            'auth_status': self.request.user.auth_status,
        }
        return Response(data, status=200)

class ChangeUserPhotoView(APIView):
    permission_classes = [IsAuthenticated, ]
    def put(self, request, *args, **kwargs):
        serializer = ChangeUserPhotoSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            serializer.update(user, serializer.validated_data)
            return Response(
                {
                    "message": "The image has been successfully changed."
                }, status=200
            )
        return Response(
            serializer.errors, status=400
        )

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class TokenRefreshView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer

class LogoutView(APIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        try:
            refresh_token = self.request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            data = {
                'success': True,
                'message': 'You are logged out.'
            }
            return Response(data, status=200)
        except TokenError:
            return Response(status=400)

class ForgotPasswordView(APIView):
    permission_classes = [AllowAny, ]
    serializer_class = ForgotPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        email_or_phone = serializer.validated_data.get('email_or_phone')
        user = serializer.validated_data.get('user')
        if check_email_or_phone(email_or_phone) == 'phone':
            code = user.create_verify_code(VIA_PHONE)
            send_email(email_or_phone, code)
        elif check_email_or_phone(email_or_phone) == 'email':
            code = user.create_verify_code(VIA_EMAIL)
            send_email(email_or_phone, code)

        return Response(
            {
                'success': True,
                'message': 'Verification code sent.',
                'access': user.token()['access'],
                'refresh': user.token()['refresh_token'],
                'user_status': user.auth_status
            }, status=200
        )

class ResetPasswordView(UpdateAPIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['patch', 'put']

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        response = super(ResetPasswordView, self).update(request, *args, **kwargs)
        try:
            user = User.objects.get(id=response.data.get('id'))
        except ObjectDoesNotExist as e:
            raise NotFound(detail="User not found.")
        return Response(
            {
                'success': True,
                'message': 'Password changed successfully.',
                'access': user.token()['access'],
                'refresh': user.token()['refresh_token']
            }
        )