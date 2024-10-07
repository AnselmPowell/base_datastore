from django.http import JsonResponse
from django.db import connections
from django.db.utils import OperationalError
from django.core.cache import cache
from redis.exceptions import RedisError
import logging

logger = logging.getLogger(__name__)

def health_check(request):
    health_status = {
        "status": "healthy",
        "database": "up",
        "cache": "up",
        "errors": []
    }

    # Check database connection
    try:
        connections['default'].cursor()
    except OperationalError:
        health_status["database"] = "down"
        health_status["status"] = "unhealthy"
        health_status["errors"].append("Database connection failed")

    # Check cache (assuming you're using Redis)
    try:
        cache.set('health_check', 'OK', 10)
        if cache.get('health_check') != 'OK':
            raise RedisError("Cache test failed")
    except RedisError as e:
        health_status["cache"] = "down"
        health_status["status"] = "unhealthy"
        health_status["errors"].append(f"Cache error: {str(e)}")

    # Check for critical services (example)
    try:
        # Assuming you have a CriticalService model
        from .models import CriticalService
        critical_services = CriticalService.objects.filter(is_active=True)
        health_status["critical_services"] = {
            service.name: "up" for service in critical_services
        }
    except Exception as e:
        health_status["status"] = "unhealthy"
        health_status["errors"].append(f"Critical service check failed: {str(e)}")

    # Log errors if any
    if health_status["errors"]:
        logger.error(f"Health check failed: {', '.join(health_status['errors'])}")

    status_code = 200 if health_status["status"] == "healthy" else 503
    return JsonResponse(health_status, status=status_code)