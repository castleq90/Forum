from django.contrib.auth import authenticate

from rest_framework                  import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User

class UserSignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            name         = validated_data['name'],
            email        = validated_data['email'],
            password     = validated_data['password'],
        )
        return user

class UserSignInSerializer(serializers.Serializer):
    id           = serializers.IntegerField(read_only=True)
    email        = serializers.EmailField()
    password     = serializers.CharField(write_only=True)
    access_token = serializers.ReadOnlyField()

    def validate(self, attrs):
        user = authenticate(**attrs)
        token = RefreshToken.for_user(user)
        attrs['id'] = user.id
        attrs['access_token'] = str(token.access_token)
        return attrs
