from django import forms
from .models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        #fields = ['description', 'publish_date', 'issuer_id', 'issue_start_date', 'issue_end_date']
        fields = '__all__'

        widgets = {
        'issue_start_date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'issue_end_date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }