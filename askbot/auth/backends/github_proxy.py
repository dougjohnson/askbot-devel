from django.contrib.auth.backends import RemoteUserBackend


class GithubProxyBackend(RemoteUserBackend):

    def configure_user(self, user):

        user.first_name = 'Doug'
        user.last_name = 'Johnson'
        user.email = 'doug.johnson@sage.com'

        return user
