from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Module, Lesson
from .forms import CourseForm, ModuleForm, LessonForm
from courses.models import Course


@login_required
def instructor_course_list(request):
    courses = Course.objects.filter(instructor=request.user)
    return render(request, 'courses/instructor_course_list.html', {'courses': courses})


@login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user
            course.save()
            # return redirect('instructor_course_list')
            return redirect('update_course', course_id=course.id)  # ✅ Redirect to edit
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', {'form': form})


@login_required
def update_course(request, course_id):
    course = get_object_or_404(Course, id=course_id, instructor=request.user)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('instructor_course_list')
    return render(request, 'courses/course_form.html', {'form': form})


@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id, instructor=request.user)
    if request.method == 'POST':
        course.delete()
        return redirect('instructor_course_list')
    return render(request, 'courses/confirm_delete.html', {'object': course})


# Modules
@login_required
def add_module(request, course_id):
    course = get_object_or_404(Course, id=course_id, instructor=request.user)
    form = ModuleForm(request.POST or None)
    if form.is_valid():
        module = form.save(commit=False)
        module.course = course
        module.save()
        return redirect('update_course', course_id=course.id)
    return render(request, 'courses/module_form.html', {'form': form, 'course': course})

@login_required
def edit_module(request, module_id):
    module = get_object_or_404(Module, id=module_id, course__instructor=request.user)
    form = ModuleForm(request.POST or None, instance=module)
    if form.is_valid():
        form.save()
        return redirect('update_course', course_id=module.course.id)
    return render(request, 'courses/module_form.html', {'form': form, 'course': module.course})

@login_required
def delete_module(request, module_id):
    module = get_object_or_404(Module, id=module_id, course__instructor=request.user)
    if request.method == 'POST':
        course_id = module.course.id
        module.delete()
        return redirect('update_course', course_id=course_id)
    return render(request, 'courses/confirm_delete.html', {'object': module})


# Lessons
@login_required
def add_lesson(request, module_id):
    module = get_object_or_404(Module, id=module_id, course__instructor=request.user)
    form = LessonForm(request.POST or None)
    if form.is_valid():
        lesson = form.save(commit=False)
        lesson.module = module
        lesson.save()
        return redirect('update_course', course_id=module.course.id)
    return render(request, 'courses/lesson_form.html', {'form': form, 'module': module})

@login_required
def edit_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id, module__course__instructor=request.user)
    form = LessonForm(request.POST or None, instance=lesson)
    if form.is_valid():
        form.save()
        return redirect('update_course', course_id=lesson.module.course.id)
    return render(request, 'courses/lesson_form.html', {'form': form, 'module': lesson.module})

@login_required
def delete_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id, module__course__instructor=request.user)
    if request.method == 'POST':
        course_id = lesson.module.course.id
        lesson.delete()
        return redirect('update_course', course_id=course_id)
    return render(request, 'courses/confirm_delete.html', {'object': lesson})
