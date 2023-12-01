from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView

from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import NewsPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import NewsPost

class IndexView(TemplateView):
    template_name = 'index.html'

class IndexView(ListView):
    template_name = "index.html"

    queryset = NewsPost.objects.order_by('-posted_at')

    paginate_by = 9

@method_decorator(login_required, name='dispatch')
class CreateNewsView(CreateView):
    form_class = NewsPostForm
    template_name = "post_news.html"
    success_url = reverse_lazy('news:post_done')
    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)
    
class PostSuccessView(TemplateView):
    template_name = 'post_success.html'

class CategoryView(ListView):
    template_name = 'index.html'

    paginate_by = 9

    def get_queryset(self):
        category_id = self.kwargs['category']

        categories = NewsPost.objects.filter(category = category_id).order_by('-posted_at')
        return categories
    
class UserView(ListView):
    template_name = 'index.html'
    paginate_by = 9

    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = NewsPost.objects.filter(user=user_id).order_by('-posted_at')
        return user_list