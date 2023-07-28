from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

# Create your views here.
@login_required
def profile(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.Files, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'profiles/profile.html', {'form': form})