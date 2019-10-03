from django import forms
from first.models import SignForm

class SignUp(forms.ModelForm):
    class Meta:
        model = SignForm
        fields = '__all__'