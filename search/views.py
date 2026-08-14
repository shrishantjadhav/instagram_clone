from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


def search_view(request):

    query = request.GET.get("q", "").strip()

    users = User.objects.none()

    if query:
        users = User.objects.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )

    context = {
        "query": query,
        "users": users,
    }

    return render(
        request,
        "search/search.html",
        context
    )