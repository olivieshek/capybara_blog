import os
from django.conf import settings
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.views import auth_logout
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Post
from .forms import PostForm, AuthenticateForm


class PostListView(ListView):
    # all posts
    model = Post


class PostCreateView(CreateView):
    # create post
    model = Post
    fields = "__all__"
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
