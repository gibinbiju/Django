from django import forms
from basicformapp.models import users,expense,category

class newuserform(forms.ModelForm):
    class Meta():
        model=users
        widgets = {
            'pwd': forms.PasswordInput(),
            'cpwd':forms.PasswordInput(),
        }
        # exclude=['field1','field2']
        # field=('field1','field2')
        fields='__all__'

        def clean(self):
            cleaned_data = super().clean()
            Name = cleaned_data.get("username")
            if users.objects.filter(username=Name):
                print("user name already exists")
                msg = "user name already exists!"
                self.add_error('username', msg)


class login(forms.ModelForm):
    class Meta():
        model =users
        widgets = {
            'pwd': forms.PasswordInput(),
        }
        exclude = ('email','phone')

        def clean(self):
            cleaned_data = super().clean()
            # pwd = cleaned_data.get("pwd")
            # cpwd = cleaned_data.get("cpwd")
            Name = cleaned_data.get("uname")
            PW = cleaned_data.get("pwd")
            if users.objects.filter(username=Name):
                print("valid user name")
            else:
                print("invalid username")
                msg1 = "invalid username"
                self.add_error('username', msg1)

            if users.objects.filter(pwd=PW):
                print("valid password")
            else:
                msg2 = "invalid password"
                self.add_error('pwd', msg2)


class expenseform(forms.ModelForm):
    class Meta():
        model = expense
        fields=['category_name','amount']

        # def form_valid(self, form):
        #     form.instance.name = self.request.user
        #     return super().form_valid(form)
class searchform(forms.ModelForm):
    class Meta():
        model = expense
        fields=['dates']
        widgets={
            'dates':forms.SelectDateWidget,
        }