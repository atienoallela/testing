from django import forms

from portfolio.models import Contact


class FeedbackForm(forms.ModelForm):
    # inner class that contains metadata
    class Meta:
        model = Contact
        fields = '__all__'
