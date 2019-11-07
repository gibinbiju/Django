from django import forms
class primeform(forms.Form):
    l=forms.IntegerField(label='Lower_Limit')
    u=forms.IntegerField(label='Upper_Limit')