from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm 
from django.contrib.auth.decorators import login_required#use for profile @required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})
@login_required
def dashboard(request):
    return render(request,
    'account/dashboard.html',
    {'section': 'dashboard'}) 
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(instance=request.user,data=request.POST)
        p_form = ProfileUpdateForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'account/profile.html',context)

