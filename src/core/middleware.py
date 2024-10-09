from django.http import HttpResponseForbidden
from django.conf import settings

class BlockSpecificDomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.blocked_domains = getattr(settings, 'BLOCKED_DOMAINS', [])

    def __call__(self, request):
        origin = request.headers.get('Origin', '')
        if any(blocked_domain in origin for blocked_domain in self.blocked_domains):
            return HttpResponseForbidden("Access from this domain is not allowed.")
        return self.get_response(request)