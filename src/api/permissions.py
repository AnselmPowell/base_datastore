from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class AllowSpecificDomainPermission(BasePermission):
    def has_permission(self, request, view):
        allowed_domains = [
            'basedatastore-production.up.railway.app'
            'https://basedatastore-production.up.railway.app',
            'http://basedatastore-production.up.railway.app'
            'baseinterface-production.up.railway.app',
            'https://baseinterface-production.up.railway.app',
            'http://baseinterface-production.up.railway.app',
            # Add more allowed domains here
        ]
        
        origin = request.headers.get('Origin')
        referer = request.headers.get('Referer')
        
        # Check if the request is coming from an allowed origin
        if origin and any(domain in origin for domain in allowed_domains):
            return True
        
        # If no Origin, check Referer as a fallback
        if not origin and referer and any(domain in referer for domain in allowed_domains):
            return True
        
        # If neither Origin nor Referer match allowed domains, deny access
        raise PermissionDenied("Access denied. Invalid origin.")