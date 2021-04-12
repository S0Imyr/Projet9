from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import CharField, Value
from django.contrib.auth.decorators import login_required

from itertools import chain

from authentification.models import User
from review.models import Ticket, Review, UserFollows
from review.forms import TicketForm, ReviewForm, TicketReviewForm


def get_followed_user(user):
    followed_users=[]
    for link in UserFollows.objects.filter(user=user):
        followed_users.append(link.followed_user)
    return followed_users


def get_followers(user):
    followers=[]
    for link in UserFollows.objects.filter(followed_user=user):
        followers.append(link.user)
    return followers


def get_users_viewable_tickets(user):
    tickets = []
    followed_users = get_followed_user(user)
    followed_users.append(user)
    for followed_user in followed_users:
        tickets.extend(Ticket.objects.filter(user=followed_user))
    return tickets


def get_users_viewable_reviews(user):
    reviews = []
    followed_users = get_followed_user(user)
    followed_users.append(user)
    my_tickets = Ticket.objects.filter(user=user)
    for ticket in my_tickets:
        relative_reviews = Review.objects.filter(ticket=ticket)
        for review in relative_reviews:
            if review.user not in followed_users:
                reviews.append(review)
    for followed_user in followed_users:
        reviews.extend(Review.objects.filter(user=followed_user))
    return reviews


def annotate_post(posts):
    response = []
    for post in posts:
        if isinstance(post, Ticket):
            obj = {'content': post, 'type': 'TICKET'}
        elif isinstance(post, Review):
            obj = {'content': post, 'type': 'REVIEW'}
        response.append(obj)
    return response


@login_required(login_url='home')
def flux(request):
    tickets = get_users_viewable_tickets(request.user)
    reviews = get_users_viewable_reviews(request.user)
    for ticket in tickets:
        if Review.objects.filter(ticket=ticket):
            ticket.answered = True
    posts = sorted(chain(tickets, reviews),
                      key=lambda post: post.time_created,
                      reverse=True)
    context = {'posts': annotate_post(posts)}
    return render(request, 'flux.html', context)


@login_required(login_url='home')
def create_ticket(request, id_ticket=None):
    if id_ticket is not None:
        ticket = get_object_or_404(Ticket, pk=id_ticket)
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
        else:
            return render(request, 'addticket.html', {'form': form})


@login_required(login_url='home')
def modify_ticket(request, id_ticket):
    context = {}
    ticket = get_object_or_404(Ticket, pk=id_ticket)
    if request.method == 'GET':
        if ticket is None:
            pass
        else:
            form = TicketForm(instance=ticket)
            context['form'] = form
        return render(request, 'addticket.html', context)
    elif request.method == 'POST':
        print(request.POST)
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('posts')

@login_required(login_url='home')
def delete_ticket(request, id_ticket):
    ticket = get_object_or_404(Ticket, pk=id_ticket)
    ticket.delete()
    return redirect('posts')


@login_required(login_url='home')
def create_review(request, id_ticket=None):
    review = None
    context = {}
    if id_ticket is not None:
        ticket = get_object_or_404(Ticket, pk=id_ticket)
        context = {'post': {'content': ticket}}
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
            ticket.save()
            return redirect('flux')
        else:
            return render(request, 'addreview.html', context)


@login_required(login_url='home')
def modify_review(request, id_review):
    context = {}
    review = get_object_or_404(Review, pk=id_review)
    if request.method == 'GET':
        if review is None:
            pass
        else:
            form = ReviewForm(instance=review)
            context['form'] = form
        return render(request, 'addreview.html', context)
    elif request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('posts')

@login_required(login_url='home')
def delete_review(request, id_review):
    review = get_object_or_404(Review, pk=id_review)
    review.ticket.answered = False
    review.delete()
    return redirect('posts')


@login_required(login_url='home')
def create_ticketreview(request):
    context = {}
    if request.method == 'GET':
        form = TicketReviewForm()
        return render(request, 'addticketreview.html', {'form': form})
    elif request.method == 'POST':
        data = request.POST
        ticket_form = TicketForm({'title': data['ticket_title'],
                                  'user': request.user,
                                 'description': data['ticket_description'],
                                 'image': data['ticket_image']})
        if ticket_form.is_valid():
            ticket = ticket_form.save()
            review_form = ReviewForm({'ticket': ticket,
                                      'rating': data['review_rating'],
                                      'headline': data['review_headline'],
                                      'body': data['review_body'],
                                      'user': request.user})
            if review_form.is_valid():
                review_form.save()
                return redirect('flux')
 

@login_required(login_url='home')
def follow(request):
    context = {}
    if request.method == 'GET':
        followed_users = get_followed_user(request.user)
        followers = get_followers(request.user)
        context = {'followed_users': followed_users, 'followers': followers}
        return render(request, 'follow.html', context)
    elif request.method == 'POST':
        new_followed_user = User.objects.filter(username=request.POST['new_followed_user'])[0]
        if new_followed_user:
            UserFollows.objects.create(user=request.user, followed_user=new_followed_user)
        return redirect('follow')


@login_required(login_url='home')
def delete_follow(request, id_followed_user):
    followed_user = get_object_or_404(User, pk=id_followed_user)
    link = get_object_or_404(UserFollows, user=request.user, followed_user=followed_user)
    link.delete()
    return redirect('follow')


@login_required(login_url='home')
def posts(request):
    tickets = Ticket.objects.filter(user=request.user)
    reviews = Review.objects.filter(user=request.user)
    for ticket in tickets:
        if Review.objects.filter(ticket=ticket):
            ticket.answered = True
    posts = sorted(chain(tickets, reviews),
                      key=lambda post: post.time_created,
                      reverse=True)
    context = {'posts': annotate_post(posts)}
    return render(request, 'posts.html', context)