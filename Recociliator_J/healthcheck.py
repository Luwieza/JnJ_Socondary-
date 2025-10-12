#!/usr/bin/env python
"""
Production health check script for Johnson & Johnson Vision Care application.
Validates deployment configuration and database connectivity.
"""
import os
import sys
import django
from django.core.management import call_command
from django.db import connection
from django.conf import settings


def health_check():
    """Comprehensive health check for production deployment"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Recociliator_J.settings')
    django.setup()
    
    print("🏥 Johnson & Johnson Vision Care - Health Check")
    print("=" * 50)
    
    checks_passed = 0
    total_checks = 7
    
    # 1. Database connectivity
    print("\n1️⃣ Testing database connection...")
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            if result[0] == 1:
                print("✅ Database connection successful")
                if 'postgresql' in settings.DATABASES['default']['ENGINE']:
                    print("   📊 Using PostgreSQL (Production Ready)")
                else:
                    print("   📋 Using SQLite (Development)")
                checks_passed += 1
            else:
                print("❌ Database connection failed")
    except Exception as e:
        print(f"❌ Database error: {e}")
    
    # 2. Environment configuration
    print("\n2️⃣ Checking environment configuration...")
    if not settings.DEBUG:
        print("✅ DEBUG disabled (production mode)")
        checks_passed += 1
    else:
        print("⚠️  DEBUG enabled (development mode)")
    
    # 3. Secret key security
    print("\n3️⃣ Validating secret key...")
    if len(settings.SECRET_KEY) >= 50 and not settings.SECRET_KEY.startswith('django-insecure'):
        print("✅ Secret key is secure")
        checks_passed += 1
    else:
        print("⚠️  Secret key may not be production-ready")
    
    # 4. Allowed hosts
    print("\n4️⃣ Checking allowed hosts...")
    if settings.ALLOWED_HOSTS and settings.ALLOWED_HOSTS != ['*']:
        print(f"✅ Allowed hosts configured: {settings.ALLOWED_HOSTS}")
        checks_passed += 1
    else:
        print("⚠️  Allowed hosts may need configuration")
    
    # 5. Static files
    print("\n5️⃣ Checking static files configuration...")
    if hasattr(settings, 'STATIC_ROOT') and settings.STATIC_ROOT:
        print("✅ Static files root configured")
        checks_passed += 1
    else:
        print("⚠️  Static files root not configured")
    
    # 6. Security middleware
    print("\n6️⃣ Validating security middleware...")
    required_middleware = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
    ]
    
    middleware_ok = all(mw in settings.MIDDLEWARE for mw in required_middleware)
    if middleware_ok:
        print("✅ Security middleware properly configured")
        checks_passed += 1
    else:
        print("❌ Security middleware missing")
    
    # 7. Application URLs
    print("\n7️⃣ Testing application URLs...")
    try:
        from django.urls import reverse
        from django.test import Client
        
        client = Client()
        response = client.get('/')
        if response.status_code in [200, 302]:  # 302 is redirect, also OK
            print("✅ Application URLs responding")
            checks_passed += 1
        else:
            print(f"⚠️  Application returned status {response.status_code}")
    except Exception as e:
        print(f"❌ URL test failed: {e}")
    
    # Summary
    print("\n" + "=" * 50)
    print(f"Health Check Results: {checks_passed}/{total_checks} checks passed")
    
    if checks_passed == total_checks:
        print("🎉 All systems go! Application is production-ready.")
        return True
    elif checks_passed >= total_checks - 2:
        print("⚠️  Application is mostly ready. Review warnings above.")
        return True
    else:
        print("❌ Application needs attention before production deployment.")
        return False


def database_info():
    """Display detailed database information"""
    print("\n📊 Database Information:")
    print("-" * 30)
    
    db_config = settings.DATABASES['default']
    print(f"Engine: {db_config.get('ENGINE', 'Not configured')}")
    
    if 'postgresql' in db_config.get('ENGINE', ''):
        print("Type: PostgreSQL (Production)")
        if 'DATABASE_URL' in os.environ:
            print("Configuration: Environment variable (Railway/Heroku)")
        else:
            print("Configuration: Manual settings")
    else:
        print("Type: SQLite (Development)")
        print(f"Location: {db_config.get('NAME', 'Not specified')}")
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT version()" if 'postgresql' in db_config.get('ENGINE', '') else "SELECT sqlite_version()")
            version = cursor.fetchone()[0]
            print(f"Version: {version}")
    except Exception as e:
        print(f"Version check failed: {e}")


if __name__ == '__main__':
    success = health_check()
    database_info()
    
    if '--verbose' in sys.argv:
        print(f"\n🔧 Django Version: {django.get_version()}")
        print(f"🐍 Python Version: {sys.version}")
        print(f"📁 Base Directory: {settings.BASE_DIR}")
    
    sys.exit(0 if success else 1)