from django import forms
from django.core import validators


# Create a validation check and pass it to a form field
# name = forms.CharField(validators=[check_for_z])
"""
def check_for_z(value):
    if value[0].lower() != "z":
        raise forms.ValidationError("NAME NEEDS TO START WITH A 'Z' !!!")
"""

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    
    #Catching bots
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)]) # built-in validators
    
    # Verifying email, enter again
    verify_email = forms.EmailField(label='Enter your email again: ')
    
    # Make sure emails match
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        
        if email != vmail:
            raise forms.ValidationError("Emails don't match")
     
    text = forms.CharField(widget=forms.Textarea)
    
    # Not using built-in validators
    """
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("GOTCHA BOT")
        return botcatcher
    """