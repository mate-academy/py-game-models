import os
import django


def setup_django():
    """
    Настройка Django-окружения.
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    django.setup()
