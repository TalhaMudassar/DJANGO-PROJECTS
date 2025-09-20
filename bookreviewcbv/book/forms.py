from django import forms 
from book.models import Book
from django.core.exceptions import ValidationError

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','description','genre','isbn','publication_date']
        widgets = {
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Book Title'
            }),
            'author':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter author name'
            }),
            'description':forms.Textarea(attrs={
                'class':'form-control',
                'rows': 4,
                'placeholder': 'Enter book description'
            }),
            'genre':forms.Select(attrs={
                'class':'form-control'
            }),
            'isbn':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter ISBN'
            }),
            'publication_date':forms.DateInput(attrs={
                'class':'form-control',
                'type': 'date'
            })
        }
    
    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if not isbn.isdigit():
            raise ValidationError("ISBN must only contain digits.")
        if len(isbn) != 13:
            raise ValidationError("ISBN must be exactly 13 digits long.")
        return isbn