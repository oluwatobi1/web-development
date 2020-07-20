from django import forms
from blog_app.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'author', 'text')
        model = Post

        widgets = {
            'title':forms.TextInput(attrs = {'class':'textinputclass'}),
            'text':forms.Textarea(attrs = {'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        fields = ('author', 'text')
        model = Comment
        widgets = {
            'author':forms.TextInput(attrs = {'class':'textinputclass'}),
            'text':forms.Textarea(attrs = {'class':'editable medium-editor-textarea'})
        }
