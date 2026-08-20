from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

from apps.core.exceptions.jwt_exception import JWTException


def error_handler(exc: Exception, context: dict):
    response = exception_handler(exc, context)

    if isinstance(exc, JWTException):
        return Response(
            {
                'detail': 'JWT expired or invalid'
            },
            status=status.HTTP_401_UNAUTHORIZED,
        )

    return response