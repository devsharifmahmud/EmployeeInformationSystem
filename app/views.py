from django.shortcuts import render
from forms import EmployeeForm

# Create your views here.
def Home(request):
    form = EmployeeForm()
    return render(request, 'apps/index.html')
