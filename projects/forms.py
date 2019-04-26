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
        try:
            if "github.com/" not in data['github_url']:
                raise forms.ValidationError("You must provide a link to a GitHub repository!")
        except:
            raise forms.ValidationError("You must provide a link to a GitHub repository!")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ["display_name",
                  "display_picture",
                  "graduation_year",
                  "pillar",
                  "bio",
                  "contact_email",
                  "personal_links"]

    def save(self, user=None):
        user_profile = super(UserProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile

class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ["title",
                  "caption",
                  "featured_image",
                  "url",
                  "poster_url"]

    def save(self, project=None):
        project_edit = super(ProjectEditForm, self).save(commit=False)
        if project:
            project_edit.project = project
        project_edit.save()
        return project_edit
