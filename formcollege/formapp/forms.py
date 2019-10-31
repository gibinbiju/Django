from django import forms
class clgform(forms.Form):
    name=forms.CharField(label='name',max_length=100)
    address=forms.CharField(label='addr',max_length=50)
    course=forms.CharField(label='course',max_length=50)
    def clean(self):
        cleaned_data=super().clean()
        course=cleaned_data.get("course")
        if course.isalpha()==False:
            raise forms.ValidationError("You entered an integer")
