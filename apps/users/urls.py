from rest_framework import routers

from apps.users.views import UserSignUpViewset, UserSignInViewset

router = routers.DefaultRouter()
router.register(r'signup', UserSignUpViewset)
router.register(r'signin', UserSignInViewset)
urlpatterns = router.urls