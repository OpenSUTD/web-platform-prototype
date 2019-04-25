from django import forms

from . import models

class SubmissionForm(forms.Form):
    project_name = forms.CharField(label="Project Name", max_length=100)
    caption = forms.CharField(label="Caption", max_length=200)
    category = forms.ChoiceField(
        label="Category",
        widget=forms.RadioSelect,
        choices=models.CATEGORY_CHOICES,
    )
    featured_image = forms.URLField(label="Featured Image", max_length=200)
    github_url = forms.URLField(label="GitHub URL", max_length=200)
    poster_url = forms.URLField(label="Poster URL", max_length=200)

    def clean(self):
        data = self.cleaned_data
        if "github.com/" not in data['github_url']:
            raise forms.ValidationError("You must provide a link to a GitHub repository!")

    