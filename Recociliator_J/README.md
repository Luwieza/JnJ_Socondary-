# Johnson & Johnson Vision Care - Lens Rejection Calculator

A professional Django web application for calculating lens rejection rates and split analysis in the Johnson & Johnson Vision Care manufacturing process.

![J&J Vision Care](https://logos-world.net/wp-content/uploads/2020/09/Johnson-Johnson-Logo.png)

## 🏢 About

This application provides a streamlined interface for lens quality control calculations, featuring:

- **Split Number Analysis**: Determine final vs non-final split processing
- **Rejection Rate Calculations**: Calculate precise rejection percentages
- **Professional UI**: Johnson & Johnson branded interface with corporate imagery
- **Mobile Responsive**: Optimized for desktop and mobile devices
- **Real-time Validation**: Form validation with clear error messaging

## 🚀 Features

- ✅ **Interactive Forms**: Step-by-step guided input process
- ✅ **Calculation Engine**: Built-in logic for lens rejection analysis
- ✅ **Professional Design**: J&J Vision Care branding and colors
- ✅ **Mobile Optimized**: Responsive design with iOS compatibility fixes
- ✅ **Session Management**: Maintains user data across form steps
- ✅ **Error Handling**: Comprehensive validation and error reporting

## 🛠️ Technology Stack

- **Backend**: Django 5.2.1
- **Database**: SQLite (development), PostgreSQL ready
- **Frontend**: HTML5, CSS3, Mobile-first responsive design
- **Python**: 3.12+
- **Styling**: Custom CSS with J&J brand colors (#dc3545, #0056b3)

## 📋 Requirements

```
Django==5.2.1
sqlparse==0.5.3
asgiref==3.8.1
```

## 🔧 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Luwieza/JnJ_Socondary-.git
cd JnJ_Socondary-/Recociliator_J
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Start Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

## 🎯 Usage

### Basic Workflow

1. **Split Number Input**: Enter the split number and confirm if it's a final split
2. **Route Selection**: System automatically routes to appropriate form (Yes/No)
3. **Data Entry**: Complete the relevant calculation form
4. **Results**: View calculated rejection rates and analysis

### Form Types

- **Final Split (Yes)**: For final processing calculations
- **Non-Final Split (No)**: For intermediate processing analysis

## 📁 Project Structure

```
Recociliator_J/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── db.sqlite3               # Development database
├── tools/
│   └── inline_bg.py         # Background image inlining utility
├── recociliator/            # Main application
│   ├── models.py            # Data models
│   ├── views.py             # Main view controllers
│   ├── calculation_views.py # Calculation logic views
│   ├── yes_views.py         # Final split views
│   ├── no_views.py          # Non-final split views
│   ├── urls.py              # URL routing
│   ├── form.py              # Form definitions
│   ├── Logic/
│   │   └── logic.py         # Core calculation algorithms
│   ├── templates/           # HTML templates
│   │   ├── split_number.html
│   │   ├── yes.html
│   │   ├── no.html
│   │   └── ...
│   └── static/              # Static assets
│       ├── styles.css       # Main stylesheet (with inlined background)
│       └── images/          # Image assets
└── Recociliator_J/          # Project settings
    ├── settings.py          # Django configuration
    ├── urls.py              # Root URL configuration
    └── wsgi.py              # WSGI application
```

## 🎨 Design Features

- **Corporate Branding**: J&J Vision Care colors and logo integration
- **Background**: Johnson & Johnson Vision Care Ireland building imagery (inlined)
- **Responsive Layout**: Flexbox-based centering with mobile optimization
- **Accessibility**: Reduced motion support and proper contrast ratios
- **Modern UI**: Glassmorphism effects with backdrop filters

## 🔒 Security Features

- CSRF protection on all forms
- Session-based data management
- Input validation and sanitization
- Secure static file serving

## 🧪 Testing

Run the development server and test the calculation workflows:

```bash
python manage.py runserver
```

Navigate through:

1. Split number entry (`/`)
2. Yes/No confirmation
3. Form completion (`/split-yes/` or `/split-no/`)
4. Results verification

## 🔧 Utilities

### Background Image Inlining

The project includes a utility to inline the background image:

```bash
python tools/inline_bg.py
```

This converts the background image to base64 and embeds it directly in the CSS for faster loading.

## 🚀 Deployment

### Production Configuration

For production deployment:

1. Set environment variables:

```bash
export SECRET_KEY="your-production-secret-key"
export DEBUG=False
export ALLOWED_HOSTS="your-domain.com"
```

2. Collect static files:

```bash
python manage.py collectstatic
```

3. Run with production server:

```bash
gunicorn Recociliator_J.wsgi:application
```

### Railway Deployment

Ready for deployment to Railway:

1. Connect your GitHub repository
2. Railway will automatically detect Django
3. Set environment variables in Railway dashboard

### Docker Support

Docker deployment ready with standard Django containerization.

## 📊 Application Flow

```
Start (/) → Split Number Input → Confirmation →
    ├── Yes → Final Split Form → Results
    └── No → Non-Final Split Form → Results
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is proprietary software for Johnson & Johnson Vision Care operations.

## 👥 Authors

- **Luwieza** - _Initial work_ - [GitHub](https://github.com/Luwieza)

## 🏢 Johnson & Johnson Vision Care

This application supports the manufacturing quality control processes at Johnson & Johnson Vision Care Ireland.

---

**Johnson & Johnson Vision Care** - Professional Lens Rejection Calculator  
_Ensuring Quality in Vision Care Manufacturing_
