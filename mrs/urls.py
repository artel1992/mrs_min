from rest_framework.routers import DefaultRouter

from mrs.views import *

router = DefaultRouter()
router.register('dean', DeanViews, 'dean')
router.register('student', StudentViews, 'student')
router.register('teacher', TeacherViews, 'teacher')
router.register('group', GroupViews, 'group')
router.register('subject', SubjectViews, 'subject')
urlpatterns = [] + router.urls
