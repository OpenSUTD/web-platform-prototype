from django import forms

class RegistrationForm(forms.Form):

  username = forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput())
  confirm = forms.CharField(widget=forms.PasswordInput())

  def clean(self):
    username = self.cleaned_data.get('username')
    password = self.cleaned_data.get('password')
    confirm = self.cleaned_data.get('confirm')
    if confirm != password:
      raise forms.ValidationError({
        'confirm': 'Passwords mismatched'
      })
    return self.cleaned_data