from django.conf import settings
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from allauth.exceptions import ImmediateHttpResponse

from projects.models import User

class CustomGithubAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        try:
            user = User.objects.get(username=sociallogin.user.username)
            sociallogin.connect(request, user)
            raise ImmediateHttpResponse("Account already exists!!")
        except Exception as e:
            print(e)

    def populate_user(self, request, sociallogin, data):
        user = sociallogin.user
        user.display_name = data["name"]
        user.username = data["name"].replace(" ", "-").lower()
