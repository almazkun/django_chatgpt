from django import forms


class MessageForm(forms.Form):
    message = forms.CharField(
        max_length=1000,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your message"}
        ),
        required=True,
    )
