from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    specialization = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='media/teachers/', blank=False, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField()
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    students = models.ManyToManyField(Student, related_name='courses', blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    photo = models.ImageField(upload_to='media/courses/', blank=False, null=True)

    def __str__(self):
        return self.title


class Test(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='test')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=500)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    correct_option = models.PositiveSmallIntegerField(
        choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3')],
        default=1
    )
    points = models.IntegerField(default=1)

    def __str__(self):
        return self.text
