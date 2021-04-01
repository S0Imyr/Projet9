from django.shortcuts import render

from review.models import Ticket, Review

def flux(request):
    article1 = Ticket.objects.all()
    article2 = Review.objects.all()
    return render(request, 'flux.html', {'article1': article1, 'article2': article2})
