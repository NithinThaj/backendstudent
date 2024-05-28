from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, check_email

router = DefaultRouter()
router.register(r'students', StudentViewSet)


urlpatterns = [
 path('check_email/', check_email, name='check-email')
]+router.urls



# from django.urls import path
# from .views import StudentCreateView, StudentDeleteView, StudentDetailView, StudentEditView, StudentListView

# urlpatterns = [
#     path('students/', StudentListView.as_view(), name='student-list'),
#     path('students/create/', StudentCreateView.as_view(), name='student-create'),
#     path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
#     path('students/edit/<int:pk>/', StudentEditView.as_view(), name='student-edit'),
#     path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),

# ]