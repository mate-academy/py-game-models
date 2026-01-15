import os
import sys
import django


def setup_django() -> None:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    django.setup()
