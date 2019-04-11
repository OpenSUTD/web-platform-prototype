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


class SubmissionForm(forms.Form):
    project_name = forms.CharField(label="Project Name", max_length=100)
    featured_image = forms.CharField(label="Featured Image", max_length=200)
    caption = forms.CharField(label="Caption", max_length=200)
    github_url = forms.CharField(label="GitHub URL", max_length=200)
    poster_url = forms.CharField(label="Poster URL", max_length=200)