from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import TeacherListView, TeacherDetailView, StudentListView, StudentDetailView, CourseListView, CourseDetailView, TestDetailView, TestListView, TeacherViewSet, StudentViewSet, CourseViewSet, TestViewSet, QuestionViewSet, SignupView, LoginView, LogoutConfirmationView
router = DefaultRouter()

router.register(r'Teachers', TeacherViewSet)
router.register(r'Students', StudentViewSet)
router.register(r'Courses', CourseViewSet)
router.register(r'Tests', TestViewSet)
router.register(r'Questions', QuestionViewSet)

urlpatterns = [
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('tests/', TestListView.as_view(), name='test_list'),
    path('tests/<int:pk>/', TestDetailView.as_view(), name='test_detail'),

    path('', views.base, name='base'),
    path('snow/', views.snow, name='snow'),

    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutConfirmationView.as_view(), name='logout'),

    path('api/', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]
