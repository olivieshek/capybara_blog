import os
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import auth_logout
from .models import Post
from .forms import PostForm, AuthenticateForm


def index(request):
    posts = Post.objects.all().order_by("date", "time")
    for i, p in enumerate(posts):
        brief = p.body[:100]
        posts[i].summary = brief + '...' if len(p.body) > len(brief) else brief
    return render(
        request,
        "blog/index.html",
        {
            "posts": posts
        }
    )


def add_post(request):
    if request.method == "GET":
        form = PostForm()
        return render(
            request,
            "blog/add_post.html",
            {"form": form}
        )
    else:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse('blog:index')
            )
        else:
            errors = (form.errors, form.non_field_errors)
            return render(
                request,
                "blog/form_not_valid",
                {"errors": errors}
            )


def read_post(request, id):
    post = Post.objects.get(pk=id)
    return render(
        request,
        'blog/single_post.html',
        {
            'post': post
        }
    )


def edit_post(request, id):
    """
    TODO после сохранения изменений выводит соответствующее сообщение;
    TODO сам он остается на странице поста
    FIXME не удаляется старое вото поста если при редактированиии заменить новым
    """
    post = Post.objects.get(pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            message = '~ Изменения сохранены'
            return render(
                request,
                'blog/edit_post.html',
                {
                    'post': post,
                    'form': form,
                    'message': message
                }
            )
        else:
            return HttpResponse("<p>Форма не валидна.</p>")
    else:
        form = PostForm(instance=post)
    return render(
        request,
        'blog/edit_post.html',
        {
            'post': post,
            'form': form
        }
    )


def delete_post(request, id):
    """TODO delete pictures"""
    image_name = str(Post.objects.get(pk=id).image)
    file_path = os.path.join(settings.MEDIA_ROOT, image_name)
    os.remove(file_path)
    Post.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse("blog:index"))


# def authorization(request):
#     if request.method == 'GET':
#         form = AuthenticateForm()
#         return render(
#             request,
#             'blog/authorization.html',
#             {
#                 'form': form
#             }
#         )
#     else:
#         # user = authenticate(username='Moscow', password='Russia2023')
#         form = AuthenticateForm(request.POST)
#         if form.is_valid():
#             print('Авторизован')
#             print(request.POST)
#             user = User.objects.create_user(
#                 username=request.POST['name'],
#                 password=request.POST['password']
#             )
#             return HttpResponseRedirect(
#                 reverse('blog:index')
#             )
#         return render(
#             request,
#             'blog/authorization.html',
#             {
#                 'form': form
#             }
#         )


def authorization(request):
    if request.method == "POST":
        form = AuthenticateForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                print('ERROR')
            return HttpResponseRedirect(reverse("blog:index"))
        else:
            print("invalid password or login")
    form = AuthenticateForm()
    return render(
        request,
        "blog/login.html",
        {
            "form": form
        }
    )


# def authorization(request):
#     if request.method == 'POST':
#         form = AuthenticateForm(request, data=request.POST)


# if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("main:homepage")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="main/login.html", context={"login_form":form})


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('blog:index'))

