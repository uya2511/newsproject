from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView

class SignUpView(CreateView):

    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy('accounts:signup_success')
    def from_valid(self, form):

        user = form.save()
        self.object = user
        return super().form_valid(form)
    
class SignUpSuccessView(TemplateView):
    template_name = "signup_success.html"

# このViewは呼び出されたときにlogout.htmlを呼び出すためのもの
class LogoutView(LogoutView):
    tepmplate_name = "logout.html"