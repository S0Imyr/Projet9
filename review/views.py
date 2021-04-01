from django.shortcuts import render
from operator import attrgetter
from itertools import chain

from review.models import Ticket, Review

def flux(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    articles = sorted(chain(tickets, reviews),
                      key=attrgetter('time_created'))

    return render(request, 'flux.html', {'articles': articles})
