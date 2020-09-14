from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


def userprofile(request, username):
    user = get_object_or_404(User, username=username)

    number_of_votes = 0

    for post in user.posts.all():
        number_of_votes = number_of_votes + (post.number_of_votes - 1)

    return render(
        request,
        "user_profile/userprofile.html",
        {"user": user, "number_of_votes": number_of_votes},
    )


def votes(request, username):
    user = get_object_or_404(User, username=username)
    votes = user.votes.all()

    posts = []

    for vote in votes:
        posts.append(vote.post)

    return render(request, "user_profile/votes.html", {"user": user, "posts": posts})


def submissions(request, username):
    user = get_object_or_404(User, username=username)

    posts = user.posts.all()

    return render(
        request, "user_profile/submissions.html", {"user": user, "posts": posts}
    )
