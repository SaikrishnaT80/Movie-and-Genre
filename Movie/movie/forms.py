from django import forms
from movie.models import Genre,Movie

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"}),
           
            }


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control"}),
            'release_date':forms.DateInput(attrs={'type': 'date'}),
            "duration":forms.TextInput(attrs={"class":"form-controlt"}),
            "summary":forms.TextInput(attrs={"class":"form-control"}),
            
        }

