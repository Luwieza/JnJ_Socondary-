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

- Python 3.12+
- Django 5.2.1
- Virtual environment support

## 🔧 Quick Start

### 1. Clone and Setup
```bash
git clone https://github.com/Luwieza/JnJ_Socondary-.git
cd JnJ_Socondary-

# Create and activate virtual environment
python -m venv JNJ
source JNJ/bin/activate  # On Windows: JNJ\Scripts\activate

# Install dependencies
cd Recociliator_J
pip install -r requirements.txt
```

### 2. Run the Application
```bash
# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

## 📁 Project Structure

```
JnJ_Socondary-/
├── README.md                # This file
├── .vscode/                 # VS Code settings
├── JNJ/                     # Virtual environment
└── Recociliator_J/          # Django project
    ├── manage.py            # Django management
    ├── requirements.txt     # Dependencies
    ├── db.sqlite3          # Database
    ├── recociliator/       # Main app
    │   ├── views.py        # View controllers
    │   ├── models.py       # Data models
    │   ├── forms.py        # Form definitions
    │   ├── Logic/          # Calculation algorithms
    │   ├── templates/      # HTML templates
    │   └── static/         # CSS, images
    └── Recociliator_J/     # Project settings
        ├── settings.py     # Configuration
        └── urls.py         # URL routing
```

## 🎯 Usage Workflow

1. **Split Number Input**: Enter split number and confirm final/non-final
2. **Automatic Routing**: System directs to appropriate calculation form
3. **Data Entry**: Complete the relevant form fields
4. **Results**: View calculated rejection rates and analysis

## 🎨 Design Features

- **Corporate Branding**: J&J Vision Care colors and imagery
- **Mobile Responsive**: Optimized for all device sizes
- **Professional UI**: Clean, modern interface with glassmorphism effects
- **Background**: Johnson & Johnson Vision Care Ireland building (inlined)

## 🔒 Security & Production

- CSRF protection enabled
- Session-based data management
- Input validation and sanitization
- Ready for production deployment (Railway, Docker)

## 🚀 Deployment

This application is ready for deployment to:
- **Railway**: Automatic Django detection
- **Heroku**: Standard Django deployment
- **Docker**: Containerization support included

## 🧪 Testing

The application includes comprehensive form validation and calculation testing. Start the server and navigate through the workflow to verify functionality.

## 📄 License

Proprietary software for Johnson & Johnson Vision Care operations.

## 👥 Author

**Luwieza** - [GitHub Profile](https://github.com/Luwieza)

---

**Johnson & Johnson Vision Care** - Professional Lens Rejection Calculator  
*Ensuring Quality in Vision Care Manufacturing*