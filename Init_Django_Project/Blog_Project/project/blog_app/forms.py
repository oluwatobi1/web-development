from django import forms
from blog_app.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        field = ('title', 'author', 'text')
        model = Post

        widgets = {
            'title':forms.TextInput(attrs = {'class':'textinputclass'}),
            'text':forms.TextArea(attrs = {'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        field = ('author', 'text')

        widgets = {
            'author':forms.TextInput(attrs = {'class':'textinputclass'}),
            'text':forms.TextArea(attrs = {'class':'editable medium-editor-textarea'})
        }
