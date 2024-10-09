from django.http import HttpResponseForbidden

class BlockSpecificDomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        blocked_domain = 'baseinterface-production.up.railway.app'
        origin = request.headers.get('Origin', '')
        if blocked_domain in origin:
            return HttpResponseForbidden("Access from this domain is not allowed.")
        return self.get_response(request)