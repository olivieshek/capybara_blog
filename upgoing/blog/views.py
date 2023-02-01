import os
from django.utils import timezone  # время для постов
from django.urls import reverse, reverse_lazy  # реверсы для переходов между страницами
from django.contrib.auth import views as av  # аутентификация и авторизация пользователя
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
import django.views.generic as generic
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post, ModelCategory, Like
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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'text', 'category']
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


class PostDeleteView(generic.DeleteView):
    # delete post
    model = Post
    success_url = reverse_lazy("blog:index")


class ModelCategoryDetailView(generic.DetailView):
    model = ModelCategory
    template_name = 'blog/modelcategory_detail.html'


class ModelCategoryListView(generic.ListView):
    model = ModelCategory
    template_name = 'modelcategory_list.html'


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Like


class CategoryDetailView(DetailView):
    model = Category


class CategoryListView(ListView):
    model = Category


def add_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like = Like(user=request.user, post=post)
    like.save()
    return redirect('post_detail', pk=pk)


def remove_like(request, pk):
    post = get_objcect_or_404(Post, pk=pk)
    like = Like.objects.get(user=request.user, post=post)
    like.delete()
    return redirect('post_detail', pk=pk)

