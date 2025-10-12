# PostgreSQL Migration Guide
# Johnson & Johnson Vision Care - Lens Rejection Calculator

## 🐘 Upgrading to PostgreSQL

### 1. Install PostgreSQL Locally (Development)

#### macOS (using Homebrew)
```bash
brew install postgresql
brew services start postgresql

# Create database and user
psql postgres
CREATE DATABASE jnj_lens_calculator;
CREATE USER jnj_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE jnj_lens_calculator TO jnj_user;
\q
```

#### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo -u postgres psql

CREATE DATABASE jnj_lens_calculator;
CREATE USER jnj_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE jnj_lens_calculator TO jnj_user;
\q
```

### 2. Update Local Environment

Create `.env` file in your project root:
```bash
# Development PostgreSQL
DATABASE_URL=postgresql://jnj_user:secure_password@localhost:5432/jnj_lens_calculator
SECRET_KEY=your-local-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 3. Install Dependencies
```bash
source JNJ/bin/activate
pip install -r requirements.txt
```

### 4. Migrate Data (if needed)

#### Export existing SQLite data
```bash
python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission > datadump.json
```

#### Switch to PostgreSQL and migrate
```bash
# Load environment variables
export $(cat .env | xargs)

# Run migrations
python manage.py migrate

# Load data (if you had existing data)
python manage.py loaddata datadump.json
```

### 5. Production PostgreSQL (Railway)

Railway automatically provisions PostgreSQL:
- Database URL is provided via `DATABASE_URL` environment variable
- No manual setup required
- Automatic backups included

### 6. Environment Variables for Production

**Required:**
```
DATABASE_URL=postgresql://user:pass@host:port/database  # Auto-provided by Railway
SECRET_KEY=your-super-secure-production-key
DEBUG=False
ALLOWED_HOSTS=your-app.up.railway.app
```

**Optional Security (HTTPS):**
```
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_HSTS_SECONDS=31536000
```

### 7. Database Performance Settings

For high-traffic production, consider adding to settings.py:
```python
# Database connection pooling
DATABASES['default']['OPTIONS'] = {
    'MAX_CONNS': 20,
    'OPTIONS': {
        'MAX_CONNS': 20,
    }
}

# Cache configuration (optional)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'jnj_cache_table',
    }
}
```

### 8. Backup Strategy

**Railway (Automatic):**
- Daily automated backups
- Point-in-time recovery available
- Access via Railway dashboard

**Manual Backup:**
```bash
# Create backup
pg_dump $DATABASE_URL > backup_$(date +%Y%m%d).sql

# Restore from backup
psql $DATABASE_URL < backup_20251012.sql
```

### 9. Monitoring

Add to your production environment:
```python
# Database query logging (development only)
if DEBUG:
    LOGGING['loggers']['django.db.backends'] = {
        'level': 'DEBUG',
        'handlers': ['console'],
    }
```

### 10. Testing Migration

```bash
# Test with PostgreSQL
python manage.py test

# Check deployment script
python deploy.py

# Verify application
python manage.py runserver
```

---

**Next Steps:**
1. Set up local PostgreSQL
2. Test migration with development database  
3. Deploy to Railway (PostgreSQL auto-configured)
4. Monitor performance and optimize as needed

Your J&J Vision Care application is PostgreSQL-ready! 🐘