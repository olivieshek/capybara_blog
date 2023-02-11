import os
from django.conf import settings
from django.utils import timezone  # время для постов
from django.urls import reverse, reverse_lazy  # реверсы для переходов между страницами
from django.contrib.auth import views as av  # аутентификация и авторизация пользователя
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post, Category, Like
from django.contrib.auth import authenticate, login
from .forms import PostForm, AuthenticateForm, CustomUserCreationForm


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['likes'] = 'like'
        return context


class PostListView(ListView):
    model = Post
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['MEDIA_URL'] = settings.MEDIA_URL
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body', 'category', 'image']
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'body', 'category']
    success_url = reverse_lazy("blog:index")
    template_name_suffix = "_update_form"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')

#  TODO Мы тут


def sign_up(request):
    if request.method == "POST":
        if request.method == "POST":
            form = CustomUserCreationForm(data=request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect(reverse("blog:index"))
            else:
                print("invalid password or login")
    form = CustomUserCreationForm()
    return render(
        request,
        "registration/sign_up.html",
        {"form": form}
    )


class BlogLoginView(av.LoginView):
    fields = "__all__"
    template_name = "registration/login.html"


class BlogLogoutView(av.LogoutView):
    fields = "__all__"
    template_name = "blog/index.html"
    next_page = reverse_lazy('blog:index')


class CategoryDetailView(DetailView):
    model = Category


class CategoryListView(ListView):
    model = Category


def add_like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    like = Like(user=request.user, post=post)
    like.save()
    return redirect('blog:post_detail', pk=post_id)


def remove_like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    like = Like.objects.get(user=request.user, post=post)
    like.delete()
    return redirect('blog:post_detail', pk=post_id)

