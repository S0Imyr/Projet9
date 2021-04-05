from django.shortcuts import render, redirect
from django.db.models import CharField, Value

from itertools import chain

from review.models import Ticket, Review
from review.forms import TicketForm, ReviewForm


def get_users_viewable_tickets(user):
    return Ticket.objects.all()


def get_users_viewable_reviews(user):
    return Review.objects.all()


def flux(request):
    tickets = get_users_viewable_tickets(request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = get_users_viewable_reviews(request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    posts = sorted(chain(tickets, reviews),
                      key=lambda post: post.time_created,
                      reverse=True)
    context = {'posts': posts}
    return render(request, 'flux.html', context)


def create_ticket(request, id_ticket=None):
    if id_ticket is not None:
        ticket = Ticket.objects.get(pk=id_ticket)
    else:
        ticket = Ticket(user=request.user)
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


def follow(request):
    context = {}
    return render(request, 'follow.html', context)


def posts(request):
    context = {}
    return render(request, 'posts.html', context)