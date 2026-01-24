from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from blog.models import Article
from .forms import ContactForm




def home(request):
    recent_articles = (
        Article.objects.filter(is_published=True)
        .order_by("-published_at", "-created_at")[:3]
    )
    return render(request, "pages/home.html", {"recent_articles": recent_articles})


def offers(request: HttpRequest) -> HttpResponse:
    return render(request, "pages/offers.html")


def results(request: HttpRequest) -> HttpResponse:
    return render(request, "pages/results.html")


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "pages/about.html")


def contact(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                send_mail(
                    subject=f"[Jascoaching] {cd['subject']}",
                    message=f"From: {cd['name']} <{cd['email']}>\n\n{cd['message']}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_TO_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, "Message envoyé avec succès.")
                return redirect("contact")  # PRG: évite double post au refresh
            except Exception:
                messages.error(request, "Erreur lors de l’envoi du message. Réessaie plus tard.")
        else:
            messages.error(request, "Merci de corriger les champs.")
    else:
        form = ContactForm()

    return render(request, "pages/contact.html", {"form": form})
