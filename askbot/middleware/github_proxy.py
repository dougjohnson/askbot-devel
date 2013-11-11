from django.contrib.auth.middleware import RemoteUserMiddleware

class GithubProxyMiddleware(RemoteUserMiddleware):
    header = 'HTTP_REMOTE_USER'
