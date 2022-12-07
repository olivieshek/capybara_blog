from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post
from .forms import PostForm


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
    post = Post.objects.get(pk=id)
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
    Post.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse("blog:index"))
