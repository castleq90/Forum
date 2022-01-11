from rest_framework                  import mixins, viewsets, status
from rest_framework.response         import Response
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users import serializers

from apps.users.serializers import UserSignInSerializer, UserSignUpSerializer
from apps.users.models      import User

class UserSignUpViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer

class UserSignInViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSignInSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
