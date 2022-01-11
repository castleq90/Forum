from rest_framework import routers

from apps.questions.views import QuestionViewset

router = routers.DefaultRouter()
router.register(r'question', QuestionViewset)
urlpatterns = router.urls