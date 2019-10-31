from django import forms
class productform(forms.Form):
    pname=forms.CharField(label='Productname',max_length=100)
    category=forms.CharField(label='Category',max_length=50)
    price=forms.IntegerField(label='Price')
    spec=forms.CharField(label='Spec',max_length=50)