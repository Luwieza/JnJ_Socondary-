#!/usr/bin/env python
"""
Production deployment script for Johnson & Johnson Vision Care Lens Rejection Calculator
Handles database migrations, static file collection, and production checks.
"""
import os
import sys
import django
from django.core.management import execute_from_command_line
from django.conf import settings


def production_setup():
    """Run production deployment tasks"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Recociliator_J.settings')
    django.setup()

    print("🏭 Johnson & Johnson Vision Care - Production Deployment")
    print("=" * 60)

    # Check environment
    if not os.environ.get('DATABASE_URL'):
        print("⚠️  WARNING: DATABASE_URL not set. Using SQLite for development.")
    else:
        print("✅ PostgreSQL database configured")

    if settings.DEBUG:
        print("⚠️  WARNING: DEBUG=True. Set DEBUG=False for production.")
    else:
        print("✅ DEBUG disabled for production")

    # Run migrations
    print("\n📊 Running database migrations...")
    execute_from_command_line(['manage.py', 'migrate'])

    # Collect static files
    print("\n📁 Collecting static files...")
    execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])

    # Create superuser if needed (optional)
    try:
        from django.contrib.auth import get_user_model
        User = get_user_model()
        if not User.objects.filter(is_superuser=True).exists():
            print(
                "\n👤 No superuser found. Run 'python manage.py createsuperuser' after deployment.")
    except Exception as e:
        print(f"⚠️  Could not check superuser: {e}")

    print("\n✅ Production deployment complete!")
    print("🚀 Your J&J Vision Care application is ready for production.")


if __name__ == '__main__':
    production_setup()
