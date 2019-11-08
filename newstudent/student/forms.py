from django import forms
from .models import User, Feedback


class Reg_form(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
