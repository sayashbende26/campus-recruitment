from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]



from django.urls import path
from .views import StudentList, RecruiterList

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('students/', StudentList.as_view(), name='student-list'),
    path('recruiters/', RecruiterList.as_view(), name='recruiter-list'),
    path('register/student/', RegisterStudentView.as_view(), name='register-student'),
    path('register/recruiter/', RegisterRecruiterView.as_view(), name='register-recruiter'),
]
from .views import RegisterStudentView, RegisterRecruiterView

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    StudentViewSet,
    RecruiterViewSet,
    CoordinatorViewSet,
    JobViewSet,
    ApplicationViewSet,
    InterviewViewSet
)

# Create router
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'students', StudentViewSet)
router.register(r'recruiters', RecruiterViewSet)
router.register(r'coordinators', CoordinatorViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'interviews', InterviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from .views import RegisterUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('', include(router.urls)),
]

# urls.py

from .views import update_profile

urlpatterns = [
    # other routes...
    path('api/profile/update/', update_profile, name='profile-update'),
]
# urls.py

from .views import job_list, apply_job

urlpatterns = [
    # other paths
    path('api/jobs/', job_list, name='job-list'),
    path('api/jobs/<int:job_id>/apply/', apply_job, name='apply-job'),
]

    

