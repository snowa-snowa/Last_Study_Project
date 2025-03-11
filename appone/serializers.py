from rest_framework import serializers
from rest_framework.relations import SlugRelatedField, StringRelatedField
from .models import Teacher, Student, Course, Test, Question


class TeacherSerializer(serializers.ModelSerializer):

    courses = serializers.HyperlinkedRelatedField(many=True, queryset=Course.objects.all(), view_name='course-detail')

    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'last_name', 'photo', 'email', 'phone_number', 'specialization', 'date_joined', 'courses')



class StudentSerializer(serializers.ModelSerializer):

    courses = serializers.HyperlinkedRelatedField(queryset=Course.objects.all(), many=True, view_name='course-detail')

    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'enrollment_date', 'courses')



class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.HyperlinkedRelatedField(queryset=Teacher.objects.all(),view_name='teacher-detail')
    students = serializers.HyperlinkedRelatedField(queryset=Student.objects.all(), many=True, view_name='student-detail')
    test = serializers.HyperlinkedRelatedField(queryset=Test.objects.all(), view_name='test-detail')

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'photo', 'teacher', 'students', 'test', 'start_date', 'end_date')



class TestSerializer(serializers.ModelSerializer):
    course = serializers.HyperlinkedRelatedField(queryset=Course.objects.all(), view_name='course-detail')
    questions = serializers.HyperlinkedRelatedField(many=True, queryset=Question.objects.all(), view_name='question-detail')

    class Meta:
        model = Test
        fields = ('id', 'title', 'course', 'questions')



class QuestionSerializer(serializers.ModelSerializer):

    test = serializers.HyperlinkedRelatedField(queryset=Test.objects.all(), view_name='test-detail')

    class Meta:
        model = Question
        fields = ('id', 'test', 'text', 'option1', 'option2', 'option3', 'correct_option', 'points')
