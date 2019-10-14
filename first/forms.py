from django import forms
from first.models import SignForm

class SignUp(forms.ModelForm):
    class Meta:
        model = SignForm
        fields = '__all__'

class MovieForm(forms.Form):
    title = forms.CharField(max_length=50, required=True)

    def __str__(self):
        return self.title

    def get_title(self):
        return self.title