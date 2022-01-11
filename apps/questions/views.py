from django.contrib.auth.models import PermissionsMixin
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated , IsAuthenticatedOrReadOnly

from apps.questions.models import Question
from apps.questions.serializers import QuestionSerializer

class QuestionViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
