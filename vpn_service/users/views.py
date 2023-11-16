
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import UserProfileForm
from .models import UserProfile


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class DashboardView(TemplateView):
    template_name = 'users/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'], _ = UserProfile.objects.get_or_create(user=self.request.user)

        return context


@method_decorator(login_required, name='dispatch')
class UserProfileView(View):
    template_name = 'users/user_profile.html'

    def get(self, request, *args, **kwargs):
        user_profile = request.user.userprofile
        return render(request, self.template_name, {'user_profile': user_profile})


@method_decorator(login_required, name='dispatch')
class EditProfileView(View):
    template_name = 'users/update.html'

    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        form = UserProfileForm(instance=user_profile)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('users:dashboard')
        return render(request, self.template_name, {'form': form})
