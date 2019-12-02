from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm, UserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blog.models import Post, Comments


def registration_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register')

    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})


def edit_profile(request):
    user = request.user
    profile = Profile.objects.get_or_create(user=user)
    profile = Profile.objects.get(user=user)
    if request.method == "POST":
        form_prof = ProfileForm(request.POST, instance=profile)
        form_user = UserForm(request.POST, instance=user)
        if form_prof.is_valid() and form_user.is_valid():
            profile = form_prof.save(commit=False)
            profile.user = user
            profile.save()
            form_user.save()
            return redirect('show_profile', pk=user.pk)
        else:
            return redirect('edit_profile')
    else:
        form_prof = ProfileForm(instance=profile)
        form_user = UserForm(instance=user)
        return render(request, 'edit-profile.html', {'form_prof': form_prof, 'form_user': form_user})


def show_profile(request, pk):
    user = User.objects.get(pk=pk)
    current_user = request.user
    posts = Post.objects.filter(author=user)
    return render(request, 'profile-view.html', {'user': user, 'posts': posts, 'current_user': current_user})