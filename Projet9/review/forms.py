from django.forms import ModelForm

from review.models import Ticket, Review


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title','description', 'user', 'image']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['ticket', 'rating', 'headline', 'body', 'user']