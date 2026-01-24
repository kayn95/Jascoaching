from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=120,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Name",
            "id": "name",
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Email",
            "id": "email",
        })
    )
    subject = forms.CharField(
        max_length=160,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Subject",
            "id": "subject",
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Message",
            "rows": 4,
            "id": "message",
        })
    )
