# from django.contrib import auth, messages
from apps.users.forms import (UserLoinForm, UserProfileForm,
                              UserRegistrationForm)
from apps.users.models import EmailVerification, User
from common.view import TitleMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoinForm


class CreateUserView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('login')
    success_message = 'You\ve successfully signed up!'

    def get_context_data(self, **kwargs):
        context = super(CreateUserView, self).get_context_data()
        context['title'] = 'Доставка еды | Регистрация'
        return context


class UserProfileView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('base')

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['title'] = 'Доставка еды | Личный кабинет'
        return context


class EmailVerificationView(TitleMixin, TemplateView):
    template_name = 'users/email_verification.html'
    title = 'Доставка еды | Подтерждение аккаунта'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verification = EmailVerification.objects.filter(user=user, code=code)
        if email_verification.exists() and not email_verification.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('base'))


# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data = request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Congratulations! You\'ve successfully signed up')
#             return HttpResponseRedirect(reverse('login'))
#     else:
#         form = UserRegistrationForm()
#     context = {'form' : form}
#     return render(request, 'users/registration.html', context)


# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(data = request.POST, instance = request.user, files = request.FILES)
#         print(request.POST['username'])
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('profile'))
#     else:
#         form = UserProfileForm(instance = request.user)
#     context = {'title':'Store - Профиль', 'form':form}
#     return render(request, 'users/profile.html', context)


# def login(request):
#     if request.method == 'POST':
#         form = UserLoinForm(data = request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username = username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('base'))
#     else:
#         form = UserLoinForm()
#     context = {'form':form}
#     return render(request, 'users/login.html', context)
