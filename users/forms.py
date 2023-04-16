from django import forms

from users.models import StudentUser

class StudentLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class StudentRegistrForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(\
        attrs={'placeholder': 'Re-Enter Password'}))

    class Meta:
        model = StudentUser
        fields = ("username", "first_name", "student_class", "division")

        widgets = {
            "username": forms.widgets.TextInput(attrs={
                "placeholder": "Username"
            }),
            "first_name": forms.widgets.TextInput(attrs={
                "placeholder": "Full Name"
            }),
            "student_class": forms.widgets.TextInput(attrs={
                "placeholder": "Class"
            }),
            "division": forms.widgets.TextInput(attrs={
                "placeholder": "Division"
            })
        }
    
    def clean_confirm_password(self):
        data = self.cleaned_data
        if data['password'] != data['confirm_password']:
            raise forms.ValidationError('Passord dont match.')
        return data['confirm_password']