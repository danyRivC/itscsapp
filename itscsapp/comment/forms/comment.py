from django import forms
from itscsapp.comment.models.comment import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'carrer']
