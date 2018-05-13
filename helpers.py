"""
Helper funtions
"""

from django.conf import settings

from debug_toolbar.middleware import show_toolbar as debug_show_toolbar


def show_debug_toolbar(request):
    return  False
    if settings.IN_DOCKER_CONTAINER:
        return True
    else:
        return debug_show_toolbar(request)
