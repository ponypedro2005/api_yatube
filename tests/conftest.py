import os
import sys

# Добавляем корневую папку в PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Устанавливаем настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtube_api.settings')

def pytest_configure():
    """Configure pytest environment."""
    import django
    django.setup()
