import os
from django.utils import timezone  # время для постов
from django.urls import reverse, reverse_lazy  # реверсы для переходов между страницами
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView  # дженерик формы
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post, ModelCategory
from .forms import PostForm, AuthenticateForm, CustomUserCreationForm


# TODO входить в аккаунт сразу после регистрации автоматически
def sign_up(request):
    if request.method == "POST":
        if request.method == "POST":
            form = CustomUserCreationForm(data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("blog:index"))
            else:
                print("invalid password or login")
    form = CustomUserCreationForm()
    return render(
        request,
        "registration/sign_up.html",
        {"form": form}
    )


class PostListView(ListView):
    # all posts
    model = Post


class PostCreateView(CreateView):
    # create post
    model = Post
    fields = "__all__"  # обязательно либо все, либо списком
    success_url = reverse_lazy("blog:index")


class PostDetailView(DetailView):
    # read single post
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PostUpdateView(UpdateView):
    # edit post
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:index")
    template_name_suffix = "_update_form"


class PostDeleteView(DeleteView):
    # delete post
    model = Post
    success_url = reverse_lazy("blog:index")


class ModelCategoryListView(ListView):
    model = ModelCategory


def list_posts_by_category(request, slug):
    category = get_object_or_404(ModelCategory, slug=slug)
    posts = Post.objects.filter(category=category)
    return render(
        request,
        "category_posts.html",
        {
            "category_name": category.name,
            "post": posts
        }
    )


# def authorization(request):
#     if request.method == "POST":
#         form = AuthenticateForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#             else:
#                 print('ERROR')
#             return HttpResponseRedirect(reverse("blog:index"))
#         else:
#             print("invalid password or login")
#     form = AuthenticateForm()
#     return render(
#         request,
#         "blog/login.html",
#         {
#             "form": form
#         }
#     )


# def logout(request):
#     auth_logout(request)
#     return HttpResponseRedirect(reverse('blog:index'))
