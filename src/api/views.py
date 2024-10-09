from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer, AdminUserSerializer
from django.contrib.auth.models import User as AdminUser
# # from .permissions import AllowSpecificDomainPermission


# @api_view(['GET'])
# def api_root(request):
#     return Response({"message": "Welcome to the Django API DataStore"})

# @api_view(['GET', 'POST'])
# def user_list_create(request):
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def user_detail(request, pk):
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# def admin_user_list(request):
#     admin_users = AdminUser.objects.all()
#     serializer = AdminUserSerializer(admin_users, many=True)
#     return Response(serializer.data)


from django.http import HttpResponseForbidden

def check_allowed_domains(request):
    allowed_domains = [
        'baseinterface-production.up.railway.app',
        'https://baseinterface-production.up.railway.app',
        'http://baseinterface-production.up.railway.app',
        'basedatastore-production.up.railway.app',
        'https://basedatastore-production.up.railway.app',
        'http://basedatastore-production.up.railway.app',
    ]
    
    origin = request.headers.get('Origin', '')
    referer = request.headers.get('Referer', '')
    
    # if not (origin or referer):
    #     return True  # Allow requests without Origin or Referer (e.g., direct API calls)
    
    # if origin and any(domain in origin for domain in allowed_domains):
    #     return True
    
    # if referer and any(domain in referer for domain in allowed_domains):
    #     return True
    
    return False


@api_view(['GET'])
def api_root(request):
    if not check_allowed_domains(request):
        return HttpResponseForbidden("Access denied. Invalid origin.")
    return Response({"message": "Welcome to the Django API DataStore"})

@api_view(['GET', 'POST'])
def user_list_create(request):
    if not check_allowed_domains(request):
        return HttpResponseForbidden("Access denied. Invalid origin.")
    
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
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