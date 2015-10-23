from django.contrib.auth.models import User
from users.serializer import UserSerializer

class UserMixin():
    queryset = User.objects.all()
    serializer_class = UserSerializer
