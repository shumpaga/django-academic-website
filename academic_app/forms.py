from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title_en', 'title_fr', 'text_en', 'text_fr')

class ContactForm(forms.Form):
    contact_name = forms.CharField(help_text="", label="Your name", required=True)
    contact_email = forms.EmailField(help_text="", label="Your email", required=True)
    subject = forms.CharField(help_text="",
            label="What do you want to talk about ?", required=True)
    content = forms.CharField(help_text="", label="Tell me everything...",
            required=True, widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)
