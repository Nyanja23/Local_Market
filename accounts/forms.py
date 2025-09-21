from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Enter Your Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Confirm Your Password", widget=forms.PasswordInput, required=True)
    business_name = forms.CharField(label="Business Name", help_text='Leave Empty If Not Vendor', required=False)

    class Meta:
        model = CustomUser
        fields = ('username','email', 'phone_number' ,'role')
    
    def clean(self):
        clean_data = super().clean()
        password1 = clean_data['password1']
        password2 = clean_data['password2']

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords Don't Match, Try Again!!")
        return clean_data
    
    def save(self, commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user