from django import forms

from articles.models import Comment


class CommentForm(forms.ModelForm):
    """Translate the comment models into comment form"""
    class Meta:
        model = Comment
        fields = ("comment", "author")