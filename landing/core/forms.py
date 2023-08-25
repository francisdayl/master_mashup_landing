from django import forms 
from .models import Email

class NewEmailForm(forms.ModelForm):
    class Meta:
    # specify model to be used
        model = Email

        # specify fields to be used
        fields = [
            "email",
        ]
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder':'Enter your email',
               'class':'inline-block py-1 pl-2 rounded-lg border-2 border-indigo-800 focus:caret-indigo-900'}))
      
    
