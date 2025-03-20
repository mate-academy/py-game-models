import os
import django


def setup_django() -> None:
    """
    Настройка Django-окружения.

    Returns:
        None
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "your_project_name.settings")
    django.setup()
