from django.shortcuts import render
from operator import attrgetter
from itertools import chain
from django.views import generic

from review.models import Ticket, Review


def flux(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    articles = sorted(chain(tickets, reviews),
                      key=attrgetter('time_created'),
                      reverse=True)
    response = []
    for article in articles:
        response.append({"content": article, "type": isinstance(article, Ticket)})
    return render(request, 'review/flux.html', {'articles': response})
