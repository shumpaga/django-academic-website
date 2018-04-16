from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title_en', 'title_fr', 'text_en', 'text_fr')

class ContactForm(forms.Form):
    contact_name = forms.CharField(help_text="", label="Nom", required=True)
    contact_email = forms.EmailField(help_text="",
            label="Email", required=True)
    subject = forms.CharField(help_text="",
            label="Sujet", required=True)
    content = forms.CharField(help_text="", label="Détails",
            required=True, widget=forms.Textarea)
