from rest_framework import routers
from rest_framework_nested import routers as drf_router
from . import views


routers= routers.DefaultRouter()
routers.register('teachers', views.TeacherViewSet, basename='teachers')
routers.register('students', views.StudentsViewSet, basename='students')
routers.register('class_name', views.NameOfClassViewset)


attendence_router = drf_router.NestedSimpleRouter(routers, 'students', lookup='students' )
attendence_router.register('attendence', views.AttendenceViewSet, basename='attendence')

urlpatterns = routers.urls + attendence_router.urls
