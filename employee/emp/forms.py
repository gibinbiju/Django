from django import forms
class empform(forms.Form):
    companyname=forms.CharField(max_length=100)
    designation=forms.CharField(max_length=100)
    ename=forms.CharField(max_length=100)
    esal=forms.IntegerField()
