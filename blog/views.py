import os
from django.utils import timezone  # время для постов
from django.urls import reverse, reverse_lazy  # реверсы для переходов между страницами
import django.views.generic as generic
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


class PostListView(generic.ListView):
    # all posts
    model = Post


class PostCreateView(generic.CreateView):
    # create post
    model = Post
    fields = "__all__"  # обязательно либо все, либо списком
    success_url = reverse_lazy("blog:index")


class PostDetailView(generic.DetailView):
    # read single post
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PostUpdateView(generic.UpdateView):
    # edit post
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:index")
    template_name_suffix = "_update_form"


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
