from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class AllowSpecificDomainPermission(BasePermission):
    def has_permission(self, request, view):
        allowed_domain = 'baseinterface-production.up.railway.app'
        origin = request.headers.get('Origin', '')
        
        if allowed_domain not in origin:
            raise PermissionDenied("Access denied. Invalid origin.")
        
        return True