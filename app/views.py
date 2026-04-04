from django.shortcuts import render
from .forms import EmployeeForm

def Home(request):
    form = EmployeeForm()
    context = {
        'form': form,
    }
    return render(request, 'apps/index.html', context)