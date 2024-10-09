from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class AllowSpecificDomainPermission(BasePermission):
    def has_permission(self, request, view):
        allowed_domains = [
            'baseinterface-production.up.railway.app',
            'https://baseinterface-production.up.railway.app',
            'http://baseinterface-production.up.railway.app',
            'basedatastore-production.up.railway.app',
            'https://basedatastore-production.up.railway.app',
            'http://basedatastore-production.up.railway.app',
            # Add more allowed domains here
        ]
        
        # Allow access if the request is coming from the same host
        if request.get_host() in allowed_domains:
            return True
        
        origin = request.headers.get('Origin')
        referer = request.headers.get('Referer')
        
        # Check if the request is coming from an allowed origin
        if origin and any(domain in origin for domain in allowed_domains):
            return True
        
        # If no Origin, check Referer as a fallback
        if not origin and referer and any(domain in referer for domain in allowed_domains):
            return True
        
        # If it's a same-origin request (e.g., from the Django admin or API root)
        if not origin and not referer:
            return True
        
        # If none of the above conditions are met, deny access
        raise PermissionDenied("Access denied. Invalid origin.")