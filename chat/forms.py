from django import forms


class MessageForm(forms.Form):
    message = forms.CharField(max_length=1000, widget=forms.Textarea, required=True)
