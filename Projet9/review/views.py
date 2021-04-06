from django.shortcuts import render, redirect
from django.db.models import CharField, Value
from django.contrib.auth.decorators import login_required

from itertools import chain

from authentification.models import User
from review.models import Ticket, Review, UserFollows
from review.forms import TicketForm, ReviewForm


def get_users_viewable_tickets(user):
    return Ticket.objects.all()


def get_users_viewable_reviews(user):
    return Review.objects.all()


@login_required(login_url='home')
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


@login_required(login_url='home')
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


@login_required(login_url='home')
def create_review(request, id_review=None, id_ticket=None):
    review = None
    context = {}
    if id_review is not None:
        review = Review.objects.get(pk=id_review)
    if id_ticket is not None:
        ticket = Ticket.objects.get(pk=id_ticket)
        context['post'] = ticket
        review = Review(ticket=ticket, rating=None, headline=None, body=None, user=request.user, time_created=None)
    else:
        review = Review(ticket=None, rating=None, headline=None, body=None, user=request.user, time_created=None)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        context['form'] = form
        return render(request, 'addreview.html', context)
    elif request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('flux')


@login_required(login_url='home')
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


@login_required(login_url='home')
def follow(request):
    context = {}
    if request.method == 'GET':
        followed_users=[]
        for link in UserFollows.objects.filter(user=request.user):
            followed_users.append(link.followed_user)
        followers=[]
        for link in UserFollows.objects.filter(followed_user=request.user):
            followers.append(link.user)
        context = {'followed_users': followed_users, 'followers': followers}
        return render(request, 'follow.html', context)
    elif request.method == 'POST':
        new_followed_user = User.objects.filter(username=request.POST['new_followed_user'])[0]
        if new_followed_user:
            UserFollows.objects.create(user=request.user, followed_user=new_followed_user)
        return redirect('follow')


@login_required(login_url='home')
def posts(request):
    tickets = Ticket.objects.filter(user=request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = Review.objects.filter(user=request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    posts = sorted(chain(tickets, reviews),
                      key=lambda post: post.time_created,
                      reverse=True)
    context = {'posts': posts}
    return render(request, 'posts.html', context)