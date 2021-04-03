from django.shortcuts import render
from operator import attrgetter
from itertools import chain


from review.models import Ticket, Review
from review.forms import TicketForm, ReviewForm

def flux(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    articles = sorted(chain(tickets, reviews),
                      key=attrgetter('time_created'),
                      reverse=True)
    response = []
    for article in articles:
        response.append({"content": article, "type": isinstance(article, Ticket)})
    context = {'articles': response}
    return render(request, 'flux.html', context)

def create_ticket(request):
    form = TicketForm()
    return render(request, 'addticket.html', {'form': form})


def create_review(request):
    form = ReviewForm()
    return render(request, 'addreview.html', {'form': form})