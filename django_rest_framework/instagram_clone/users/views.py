from django.shortcuts import render
from .models import User, DONE, CODE_VERIFIED, NEW, VIA_EMAIL, VIA_PHONE
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from .serializers import SignUpSerializer, ChangeUserInformation
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from rest_framework.exceptions import ValidationError
from shared.utility import send_email
from django.utils import timezone

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
