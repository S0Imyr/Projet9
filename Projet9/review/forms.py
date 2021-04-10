from django import forms
from django.forms.widgets import RadioSelect
from review.models import Ticket, Review


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title','description', 'user', 'image']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['ticket', 'rating', 'headline', 'body', 'user']


class TicketReviewForm(forms.Form):
    choices = (("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5))
    ticket_title = forms.CharField(max_length=128)
    ticket_description = forms.CharField(widget=forms.Textarea)
    ticket_image = forms.ImageField()
    review_rating = forms.ChoiceField(choices=choices, widget=RadioSelect())
    review_headline = forms.CharField(max_length=128)
    review_body = forms.CharField(max_length=8192)