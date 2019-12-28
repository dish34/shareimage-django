from django import forms
from .models import Image

class PostForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('title','description','img',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control',
        'placehoder':"Give title"})
        self.fields['description'].widget.attrs.update({'class':'form-control',
            'placehoder':"Your description"})
        self.fields['img'].widget.attrs.update({'class':'btn'})