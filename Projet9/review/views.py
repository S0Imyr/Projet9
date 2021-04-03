from django.shortcuts import render, redirect
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


def create_ticket(request, id_ticket=None):
    if id_ticket is not None:
        ticket = Ticket.objects.get(pk=id_ticket)
    else:
        ticket = None
    if request.method == 'GET':
        form = TicketForm(instance=ticket)
        return render(request, 'addticket.html', {'form': form})
    elif request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('flux')


def create_review(request, id_review=None, id_ticket=None):
    review = None
    if id_review is not None:
        review = Review.objects.get(pk=id_review)
    if id_ticket is not None:
        ticket = Ticket.objects.get(pk=id_ticket)
        review = Review(ticket=ticket, rating=None, headline=None, body=None, user=None,time_created=None)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'addreview.html', {'form': form})
    elif request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('flux')


def create_ticketreview(request):
    if request.method == 'GET':
        ticketform = TicketForm()
        reviewform = ReviewForm()
        return render(request, 'addticketreview.html', {'ticketform': ticketform, 'reviewform ': reviewform })
    elif request.method == 'POST':
        ticket = TicketForm(request.POST)
        if form.is_valid():
            article = ticket.save()
            review = ReviewForm(request.POST)
            if form.is_valid():
                article = review.save()
                return redirect('flux')