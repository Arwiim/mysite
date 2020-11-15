from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25) #<input type="text">
    email = forms.EmailField() 
    to = forms.EmailField()
    comments = forms.CharField(required=False, #default widget can be overridden with thewidget attribute
                               widget=forms.Textarea)
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')