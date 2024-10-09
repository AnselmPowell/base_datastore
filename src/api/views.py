from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer, AdminUserSerializer
from django.contrib.auth.models import User as AdminUser
from django.http import HttpResponseForbidden
from urllib.parse import urlparse

import logging
import json
from pprint import pformat

logger = logging.getLogger(__name__)

def log_request_details(request):
    # Basic request information
    request_data = {
        "method": request.method,
        "path": request.path,
        "path_info": request.path_info,
        "scheme": request.scheme,
        "full_url": request.build_absolute_uri(),
        "is_secure": request.is_secure(),
        "is_ajax": request.headers.get('X-Requested-With') == 'XMLHttpRequest',
        "content_type": request.content_type,
        "content_params": request.content_params,
    }

    # Headers
    request_data["headers"] = dict(request.headers)

    # GET parameters
    request_data["GET"] = dict(request.GET)

    # POST data (be cautious with sensitive information)
    if request.method == "POST":
        try:
            request_data["POST"] = json.loads(request.body)
        except json.JSONDecodeError:
            request_data["POST"] = dict(request.POST)

    # Files
    request_data["FILES"] = {k: v.name for k, v in request.FILES.items()} if request.FILES else {}

    # Cookies
    request_data["COOKIES"] = dict(request.COOKIES)

    # Session data (if using sessions)
    if hasattr(request, 'session'):
        request_data["SESSION"] = dict(request.session)

    # META data
    meta_copy = request.META.copy()
    # Remove any sensitive information from META
    for key in ['HTTP_COOKIE', 'HTTP_AUTHORIZATION']:
        if key in meta_copy:
            del meta_copy[key]
    request_data["META"] = meta_copy

    # User information (if authenticated)
    if request.user.is_authenticated:
        request_data["USER"] = {
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
            "is_staff": request.user.is_staff,
            "is_superuser": request.user.is_superuser,
        }
    else:
        request_data["USER"] = "AnonymousUser"

    # Log the gathered information
    logger.info(f"Detailed request information:\n{pformat(request_data)}")

    return request_data

def check_allowed_domains(request):
    allowed_domains = [
        'baseinterface-production.up.railway.app',
        'https://baseinterface-production.up.railway.app',
        'http://baseinterface-production.up.railway.app',
        'basedatastore-production.up.railway.app',
        'https://basedatastore-production.up.railway.app',
        'http://basedatastore-production.up.railway.app',
    ]
    
    host = request.get_host().lower()
    origin = request.headers.get('Origin', '').lower()
    referer = request.headers.get('Referer', '').lower()

    def domain_match(url):
        parsed = urlparse(url)
        return parsed.netloc in allowed_domains or parsed.netloc.split(':')[0] in allowed_domains

    # Check if the request is coming from an allowed host
    if host in allowed_domains:
        return True

    # Check if the request has a valid Origin header
    # if origin and domain_match(origin):
    #     return True

    # If no Origin, check Referer as a fallback
    if not origin and referer and domain_match(referer):
        return True
    
    return False


@api_view(['GET'])
def api_root(request):
    if not check_allowed_domains(request):
        return HttpResponseForbidden("Access denied. Invalid origin.")
    return Response({"message": "Welcome to the Django API DataStore"})

@api_view(['GET', 'POST'])
def user_list_create(request):
    # if not check_allowed_domains(request):
    #     return HttpResponseForbidden("Access denied. Invalid origin.")

    host = request.get_host().lower()
    full_url = request.build_absolute_uri()
    parsed_url = urlparse(full_url)
    request = log_request_details

    
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        # return {"host": host, "origin": origin}
        return Response({"host": host, "request": request})
        # return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    if not check_allowed_domains(request):
        return HttpResponseForbidden("Access denied. Invalid origin.")
    
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def admin_user_list(request):
    if not check_allowed_domains(request):
        return HttpResponseForbidden("Access denied. Invalid origin.")
    
    admin_users = AdminUser.objects.all()
    serializer = AdminUserSerializer(admin_users, many=True)
    return Response(serializer.data)