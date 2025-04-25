from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from appone.models import Teacher, Student, Course, Test, Question
from rest_framework import viewsets,  filters
from .serializers import TeacherSerializer, StudentSerializer, CourseSerializer, TestSerializer, QuestionSerializer
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import View
from django.shortcuts import redirect, render
from django.db.models import Q
from django.urls import reverse_lazy
from django.db import models


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher_list.html'
    context_object_name = 'teachers'

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher_detail.html'
    context_object_name = 'teacher'


class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        course_id = self.request.GET.get('course')

        if course_id:
            queryset = queryset.filter(courses__id=course_id)  # courses — это связь ManyToManyField в модели Student

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()  # Передаем список курсов в шаблон
        return context


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'


class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'courses'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'
    context_object_name = 'course'


class TestDetailView(LoginRequiredMixin, DetailView):
    model = Test
    template_name = 'test_detail.html'
    context_object_name = 'test'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        questions = self.object.questions.all()
        score = 0
        results = []

        for question in questions:
            selected = request.POST.get(f'question_{question.id}')
            try:
                selected_int = int(selected)
            except (TypeError, ValueError):
                selected_int = None

            correct = question.correct_option

            selected_option_text = getattr(question, f'option{selected_int}', '') if selected_int else ''
            correct_option_text = getattr(question, f'option{correct}')

            if selected_int == correct:
                score += question.points

            results.append({
                'question': question,
                'selected_option': selected_int,
                'selected_option_text': selected_option_text,
                'correct_option': correct,
                'correct_option_text': correct_option_text,
            })

        context = self.get_context_data(object=self.object, submitted=True, score=score, results=results)
        return self.render_to_response(context)


class TestListView(LoginRequiredMixin, ListView):
    model = Test
    template_name = 'test_list.html'
    context_object_name = 'tests'


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'first_name', 'last_name', 'email']


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'first_name', 'last_name', 'email']


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'title']


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'title']


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'text']


class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        return render(request, 'signup.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        return render(request, 'login.html', {'form': form})


class LogoutConfirmationView(View):
    def get(self, request):
        return render(request, 'logout_confirmation.html')

    def post(self, request):
        logout(request)
        return redirect('/')


def base(request):
    courses = Course.objects.all().order_by('-start_date')[:3]
    return render(request, 'base.html',{'courses': courses})


def snow(request):
    context = ()
    return render(request, 'snow.html',{'context': context})
