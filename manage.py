#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import environ


def main():
    """Run administrative tasks."""
    # .env faylini o'qish
    environ.Env().read_env(".env")

    # DJANGO_SETTINGS_MODULE ni sozlash
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')  # 'core' ni loyihangiz nomi bilan almashtiring

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
