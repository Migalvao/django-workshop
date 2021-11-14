from django import forms


class CommentForm(forms.Form):
    author = forms.CharField(max_length=20, label="Your name")
    text = forms.CharField(label="Your comment", widget=forms.Textarea)
