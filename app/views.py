from django.shortcuts import render
from .forms import EmployeeForm

def Home(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.post)
        form.save()

    context = {
        'form': form,
    }
    return render(request, 'apps/index.html', context)