from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Post


@login_required
def fyp(request):
    posts = Post.objects.select_related("user").order_by("-created_at")

    return render(
        request,
        "fyp/fyp.html",
        {"posts": posts}
    )
