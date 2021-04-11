from django import forms
from django.forms.widgets import RadioSelect, Textarea
from review.models import Ticket, Review

CHOICES = (("0", 0), ("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5))

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title','description', 'user', 'image']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['ticket', 'rating', 'headline', 'body', 'user']
        widgets = {'rating': RadioSelect(choices=CHOICES),
                   'body': Textarea()}


class TicketReviewForm(forms.Form):
    ticket_title = forms.CharField(max_length=128)
    ticket_description = forms.CharField(widget=forms.Textarea, required=False)
    ticket_image = forms.ImageField(required=False, )
    review_rating = forms.ChoiceField(choices=CHOICES, widget=RadioSelect())
    review_headline = forms.CharField(max_length=128)
    review_body = forms.CharField(max_length=8192, widget=Textarea)