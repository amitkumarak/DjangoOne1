from django import forms

from comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content", "library_id"]
        widgets = {
            "content": forms.Textarea(),
            "library_id": forms.HiddenInput()
        }
