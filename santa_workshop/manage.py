#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from dotenv import find_dotenv, load_dotenv
from pathlib import Path 


def main():
    """Run administrative tasks."""

    current_env = os.getenv('ENV')
    if current_env:
        current_env_path = find_dotenv(f'credentials/{current_env}.env')
        load_dotenv(current_env_path, verbose=True, override=True)

    # Лучше всё-таки base
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'santa_workshop.settings.dev')

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
