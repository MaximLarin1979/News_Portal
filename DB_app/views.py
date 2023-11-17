from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import PostForm
from .filters import PostFilter
from .models import Post


class PostList(ListView, LoginRequiredMixin):
    model = Post
    ordering = '-post_time'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['time_now'] = datetime.utcnow()
        return context


class PostDetail(DetailView,LoginRequiredMixin):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/news/articles/create/':
            post.post_type = 'ar'
        elif self.request.path == '/news/news/create/':
            post.post_type = 'ne'
        return super().form_valid(form)


class PostUpdate(UpdateView, LoginRequiredMixin):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
