from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Article


def article_list(request):
    q = (request.GET.get("q") or "").strip()

    articles = Article.objects.filter(is_published=True)
    if q:
        articles = articles.filter(
            Q(title__icontains=q) | Q(excerpt__icontains=q) | Q(content__icontains=q)
        )

    return render(request, "blog/list.html", {"articles": articles, "q": q})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)

    recent_articles = (
        Article.objects.filter(is_published=True)
        .exclude(id=article.id)
        .order_by("-published_at", "-created_at")[:3]
    )

    return render(
        request,
        "blog/detail.html",
        {"article": article, "recent_articles": recent_articles},
    )
