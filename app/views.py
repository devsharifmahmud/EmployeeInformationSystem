from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee

def Home(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        form.save()
        form = EmployeeForm()

    context = {
        'form': form,
    }
    return render(request, 'apps/index.html', context)