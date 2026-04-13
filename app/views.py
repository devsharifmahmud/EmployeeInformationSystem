from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee

def Home(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        form.save()
        form = EmployeeForm()

    data = Employee.objects.all()

    context = {
        'form': form,
        'data': data
    }
    return render(request, 'apps/index.html', context)

#Delete View
def Delete_record(request, id):
    print(id)