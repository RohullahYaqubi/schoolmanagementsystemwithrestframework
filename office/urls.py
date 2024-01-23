from rest_framework import routers
from . import views


routers= routers.DefaultRouter()
routers.register('teachers', views.TeacherViewSet, basename='teachers')
routers.register('students', views.StudentsViewSet, basename='students')
routers.register('class_name', views.NameOfClassViewset)

urlpatterns = routers.urls
