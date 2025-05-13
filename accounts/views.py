from django.shortcuts import redirect, render
from huggingface_hub import login

from accounts.forms import InstructorSignUpForm, StudentSignUpForm


def student_signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('student_dashboard')  # You'll define this later
    else:
        form = StudentSignUpForm()
    return render(request, 'accounts/signup.html', {'form': form, 'role': 'Student'})

def instructor_signup(request):
    if request.method == 'POST':
        form = InstructorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('instructor_dashboard')
    else:
        form = InstructorSignUpForm()
    return render(request, 'accounts/signup.html', {'form': form, 'role': 'Instructor'})
