from rest_framework import routers

from apps.questions.views import CommentViewset, QuestionViewset

router = routers.DefaultRouter()
router.register(r'question', QuestionViewset)
router.register(r'comment', CommentViewset)
urlpatterns = router.urls