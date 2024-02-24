from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def taskform(request):
    return render(request, 'taskform.html')
def tutorial(request):
    return render(request, 'tutorial.html')
def congo(request):
    return render(request, 'congo.html')

# views.py
from django.shortcuts import render, redirect
from .forms import TaskForm

def taskform_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('congratulations')  # Redirect to a success page
    else:
        form = TaskForm()
    return render(request, 'taskform.html', {'form': form})

