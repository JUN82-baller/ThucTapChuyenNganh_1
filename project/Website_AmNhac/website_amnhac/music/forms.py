from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from .models import Album,Song,Artist,Order, Contact
from django.contrib.auth.models import User

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name']
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artist',
            'cover',
            'release_year',
            'price',
        ]

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields =['title','album','audio_file','duration',]

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email","password1","password2"]

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","password"]

SongFormSet = inlineformset_factory(
    Album, Song,
    form=SongForm,
    extra=1,
    can_delete=True   # cho phép tick để xóa bài hát
)
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["name", "email", "mobile", "address", "payment_method"]

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','subject','message']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'E-Mail'}),
            'subject':forms.TextInput(attrs={'class':'form-control','placeholder':'Subject'}),
            'message':forms.Textarea(attrs={'class':'form-control','placeholder':'Message'}),
        }
