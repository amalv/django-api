from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.app.serializers import UserSerializer
from django.core.mail import send_mail
import os

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        response = super(UserViewSet, self).create(request, *args, **kwargs)
        username = request.data.__getitem__('username')
        first_name = request.data.__getitem__('first_name')
        email = request.data.__getitem__('email')
        fromEmail = os.environ.get('SENDER_EMAIL')
        subject = "Welcome " + first_name
        body = "You have been registered with the email " + email
        send_mail(subject, body,  fromEmail, [email])
        return response
    
