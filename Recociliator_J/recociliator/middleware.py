import time
import logging

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    """Very small middleware that logs request start and end.

    This is safe for production: it only logs method/path and timings to stdout
    so Gunicorn logs will show whether a request reached Django and whether
    processing completed. Remove once debugging is finished.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        logger.info(
            f"REQUEST START {request.method} {request.get_full_path()}")
        try:
            response = self.get_response(request)
            return response
        finally:
            elapsed = (time.time() - start) * 1000.0
            logger.info(
                f"REQUEST END {request.method} {request.get_full_path()} {elapsed:.1f}ms")
