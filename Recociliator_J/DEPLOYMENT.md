# Johnson & Johnson Vision Care - Deployment Guide

## 🚀 Railway Deployment

### 1. Prepare Your Repository

```bash
# Make sure all changes are committed
git add .
git commit -m "Add production deployment configuration"
git push origin main
```

### 2. Deploy to Railway

#### Option A: GitHub Integration (Recommended)

1. Go to [Railway.app](https://railway.app/)
2. Sign up/Login with your GitHub account
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your `JnJ_Socondary-` repository
5. Railway will automatically detect Django and start building

#### Option B: Railway CLI

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway init
railway up
```

### 3. Configure Environment Variables

In your Railway dashboard, add these environment variables:

**Required:**

```
SECRET_KEY=your-super-secret-production-key
DEBUG=False
ALLOWED_HOSTS=your-railway-domain.railway.app
```

**Railway automatically provides:**

- `DATABASE_URL` (PostgreSQL)
- `PORT` (Application port)

### 4. Database Setup

Railway automatically provisions a PostgreSQL database. The app will run migrations on deployment.

### 5. Access Your Application

Your app will be available at: `https://your-app-name.up.railway.app`

## 🐳 Docker Deployment

### Local Docker Testing

```bash
# Build the image
docker build -t jnj-lens-calculator .

# Run locally
docker run -p 8000:8000 \
  -e SECRET_KEY="your-secret-key" \
  -e DEBUG=False \
  -e ALLOWED_HOSTS="localhost,127.0.0.1" \
  jnj-lens-calculator
```

### Production Docker

The included `Dockerfile` is optimized for production:

- Multi-stage build for smaller images
- Security best practices
- Static file collection
- PostgreSQL support

## 🔒 Security Configuration

### Production Settings Applied:

- Environment-based configuration
- Secure headers (XSS, Content-Type protection)
- WhiteNoise for static file serving
- PostgreSQL database support
- CSRF protection enabled

### Additional Security (Optional):

Add to your environment variables:

```
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

## 📋 Deployment Checklist

- [x] Environment variables configured
- [x] Database migrations ready
- [x] Static files collection setup
- [x] Security headers configured
- [x] Production WSGI server (Gunicorn)
- [x] Docker configuration
- [x] Railway deployment config

## 🔧 Troubleshooting

### Common Issues:

**Static files not loading:**

- Ensure `STATIC_ROOT` is configured
- Run `python manage.py collectstatic`

**Database connection errors:**

- Verify `DATABASE_URL` environment variable
- Check Railway database provisioning

**Application not starting:**

- Check Railway build logs
- Verify all environment variables are set

### Health Check

Your deployed app should respond at:

- `/` - Main application (redirects to split-number)
- `/split-number/` - Main form
- `/static/styles.css` - CSS should load

## 📞 Support

For deployment issues:

- Railway: [Railway Documentation](https://docs.railway.app/)
- Django: [Django Deployment Checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/)

---

**Johnson & Johnson Vision Care** - Production Deployment Ready
