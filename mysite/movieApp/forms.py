from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import MovieReview, Movie, User  

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class MovieReviewForm(forms.ModelForm):
    class Meta:

        model = MovieReview
        fields = ["review", "rating", "moviefK", "userfK"]
        
        def __init__(self, *args, **kwargs):
            super(MovieReviewForm, self).__init__(*args, **kwargs)

            # Set the 'disabled' attribute for moviefK and userfK fields
            self.fields['moviefK'].disabled = True
            self.fields['userfK'].disabled = True
