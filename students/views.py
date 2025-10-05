# students/views.py
from django.shortcuts import render
from .models import Student, MyModel
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import StudentForm

class StudentCreateView(CreateView):
    model = Student  # Указываем модель, с которой будет работать это представление
    form_class = StudentForm  # Указываем форму, которая будет использоваться для ввода данных
    template_name = 'student_form.html'  # Шаблон, который будет использоваться для отображения формы
    success_url = '/students/'  # URL, на который будет перенаправлен пользователь после успешной отправки формы


class StudentUpdateView(UpdateView):
    model = Student  # Указываем модель, с которой будет работать это представление
    form_class = StudentForm  # Указываем форму, которая будет использоваться для ввода данных
    template_name = 'student_form.html'  # Шаблон, который будет использоваться для отображения формы
    success_url = '/students/'  # URL, на который будет перенаправлен пользователь после успешной отправки формы


class MyModelCreateView(CreateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'students/mymodel_form.html'
    success_url = reverse_lazy('students:mymodel_list')


class MyModelListView(ListView):
    model = MyModel
    template_name = 'students/mymodel_list.html'
    context_object_name = 'mymodels'


class MyModelDetailView(DetailView):
    model = MyModel
    template_name = 'students/mymodel_detail.html'
    context_object_name = 'mymodel'

class MyModelUpdateView(UpdateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'students/mymodel_form.html'
    success_url = reverse_lazy('students:mymodel_list')


class MyModelDeleteView(DeleteView):
    model = MyModel
    template_name = 'students/mymodel_confirm_delete.html'
    success_url = reverse_lazy('students:mymodel_list')


def about(request):
    return render(request, 'students/about.html')


def index(request):
    student = Student.objects.get(id=1)
    context = {
        'student_name': f'{student.first_name} {student.last_name}',
        'student_year': student.get_year_display(),
    }
    return render(request, 'students/index.html', context)


def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    context = {'student': student}
    return render(request, 'students/student_detail.html', context)


def student_list(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students/student_list.html', context)