from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class AllowSpecificDomainPermission(BasePermission):
    allowed_domains = [
        'baseinterface-production.up.railway.app',
        'basedatastore-production.up.railway.app',
    ]

    def has_permission(self, request, view):
        host = request.get_host().lower()
        origin = request.headers.get('Origin', '').lower()
        referer = request.headers.get('Referer', '').lower()
        
        # Allow access if the request is coming from the same host
        if any(host == domain.lower() for domain in self.allowed_domains):
            return True
        
        # Check if the request is coming from an allowed origin
        if origin and any(origin.endswith(domain.lower()) for domain in self.allowed_domains):
            return True
        
        # If no Origin, check Referer as a fallback
        if not origin and referer and any(referer.endswith(domain.lower()) for domain in self.allowed_domains):
            return True
        
        # If it's a same-origin request (e.g., from the Django admin or API root)
        if not origin and not referer:
            return True
        
        # If none of the above conditions are met, deny access
        raise PermissionDenied("Access denied. Invalid origin.")