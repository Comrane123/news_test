import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import PostForm, CommentForm
from .models import Post, Vote


def frontpage(request):
    date_from = datetime.datetime.now() - datetime.timedelta(days=1)

    posts = Post.objects.filter(created_at__gte=date_from).order_by("-number_of_votes")[
        0:30
    ]

    return render(request, "post/frontpage.html", {"posts": posts})


def search(request):
    query = request.GET.get("query", "")

    if len(query) > 0:
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = []

    return render(request, "post/search.html", {"posts": posts, "query": query})


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.created_by = request.user
            comment.save()

            return redirect("post", post_id=post_id)
    else:
        form = CommentForm()

    return render(request, "post/detail.html", {"post": post, "form": form})


def newest(request):
    posts = Post.objects.all()[0:200]

    return render(request, "post/newest.html", {"posts": posts})


@login_required
def vote(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    next_page = request.GET.get("next_page", "")

    if post.created_by != request.user and not Vote.objects.filter(
        created_by=request.user, post=post
    ):
        vote = Vote.objects.create(post=post, created_by=request.user)

    if next_page == "post":
        return redirect("post", post_id=post_id)
    else:
        return redirect("frontpage")


@login_required
def submit(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()

            return redirect("frontpage")
    else:
        form = PostForm()

    return render(request, "post/submit.html", {"form": form})
