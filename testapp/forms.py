from django import forms
from django.core import validators
from testapp.models import Semester

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    v_email = forms.EmailField(label = "Enter email again")
    text = forms.CharField(widget = forms.Textarea)
#    botcatcher = forms.CharField(required = False, widget= forms.HiddenInput, validators =[validators.MaxLengthValidator(0)])

    def clean(self):
        cleandata = super().clean()
        emale = cleandata['email']
        vemale = cleandata['v_email']
        if emale != vemale:
            raise forms.ValidationError("Emails don't match!")
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA Bot!")
    #     return botcatcher
    