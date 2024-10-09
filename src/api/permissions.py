from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class AllowSpecificDomainPermission(BasePermission):
    def has_permission(self, request, view):
        allowed_domains = [
            'basedatastore-production.up.railway.app'
            'https://basedatastore-production.up.railway.app',
            'http://basedatastore-production.up.railway.app'
            'baseinterface-production.up.railway.app',
            'https://baseinterface-production.up.railway.app/',
            'http://baseinterface-production.up.railway.app/',
            # Add more allowed domains here
        ]
        origin = request.headers.get('Origin', '')
        
        if not any(domain in origin for domain in allowed_domains):
            raise PermissionDenied("Access denied. Invalid origin.")
        
        return True