from rest_framework import routers
from rest_framework_nested import routers as drf_router
from . import views


routers= routers.DefaultRouter()
routers.register('teachers', views.TeacherViewSet, basename='teachers')
routers.register('students', views.StudentsViewSet, basename='students')
routers.register('class_name', views.NameOfClassViewset)


attendence_router = drf_router.NestedSimpleRouter(routers, 'students', lookup='students' )
attendence_router.register('attendence', views.AttendenceViewSet, basename='attendence')


results_router = drf_router.NestedSimpleRouter(routers, 'students', lookup='student' )
results_router.register('results', views.ResultsOfStudentsViewSet, basename='results')

fees_router = drf_router.NestedSimpleRouter(routers, 'students', lookup='student' )
fees_router.register('fees', views.FeesOfStudentViewSet, basename='fees')

urlpatterns = routers.urls + attendence_router.urls + results_router.urls + fees_router.urls
