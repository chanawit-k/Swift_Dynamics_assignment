from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apis.views.v1 import (
    school,
    teacher,
    student
)

router = DefaultRouter()
router.register('school', school.SchoolViewSet)
router.register('classroom', school.ClassRoomViewSet)
router.register('teacher', teacher.TeacherViewSet)
router.register('student', student.StudentViewSet)
api_v1_urls = (router.urls, 'v1')

urlpatterns = [
    path('v1/', include(api_v1_urls))
]
