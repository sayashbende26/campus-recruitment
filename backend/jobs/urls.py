from rest_framework.routers import DefaultRouter
from .views import JobPostViewSet

router = DefaultRouter()
router.register(r'jobs', JobPostViewSet, basename='job')

urlpatterns = router.urls
