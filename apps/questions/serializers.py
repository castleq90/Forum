from rest_framework import serializers

from apps.questions.models import Question

class QuestionSerializer(serializers.ModelSerializer):
        class Meta:
            model = Question
            fields = ['id', 'title', 'contents', 'like_count', 'create_at', 'update_at', 'user']
            read_only_fields = ['like_count', 'user']

        # 해당 질문 작성자의 user_id값만 부여
        def create(self, validated_data):
            user = self.context['request'].user
            return Question.objects.create(user=user, **validated_data)
