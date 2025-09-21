from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form =  CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form':form})