# Linda Mama Pregnancy Journey Tracker
#### Video Demo: <URL HERE>
#### Description:

The Linda Mama Pregnancy Journey Tracker is a comprehensive web application designed to help expecting parents monitor and document their pregnancy journey. This Flask-based application provides an intuitive interface for tracking various aspects of pregnancy, from health metrics to photo documentation.

### Project Purpose

During pregnancy, parents need to track multiple aspects of their health and journey, which often involves using multiple apps or paper records. This application consolidates all essential tracking features into a single, user-friendly platform. The project aims to simplify pregnancy tracking while providing a meaningful way to document this special journey.

### Features

1. **User Authentication System**
   - Secure registration and login functionality
   - Password hashing for security
   - User-specific data isolation
   - Due date tracking and week calculation

2. **Dashboard**
   - Weekly pregnancy progress visualization
   - Quick access to all tracking features
   - Summary of recent entries
   - Baby size comparisons based on current week

3. **Health Tracking**
   - Weight monitoring with history
   - Symptom logging (nausea, fatigue, mood, headaches)
   - Movement/kick counter with timer
   - Notes and observations for each entry

4. **Appointment Management**
   - Schedule medical appointments
   - Store doctor information and locations
   - View upcoming appointments
   - Appointment deletion functionality

5. **Photo Journal**
   - Upload and store pregnancy journey photos
   - Add captions and dates
   - Automatic week labeling based on due date
   - Secure file handling and storage

### Technical Implementation

The project is built using the following technologies:

- **Backend Framework**: Flask (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF
- **File Handling**: Werkzeug utilities

### File Structure and Functionality


LindaMama/
├── app/
│   ├── init.py          # Application factory and extensions
│   ├── routes/
│   │   ├── init.py      # Blueprint registration
│   │   ├── main.py          # Main routes (home, dashboard)
│   │   ├── auth.py          # Authentication routes
│   │   └── tracking.py      # Health tracking routes
│   ├── models/
│   │   ├── init.py      # Model imports
│   │   ├── user.py          # User model
│   │   └── tracking.py      # Tracking models
│   ├── templates/           # Jinja2 templates
│   └── static/              # Static files (CSS, JS)
├── instance/                # Instance-specific files
├── migrations/              # Database migrations
├── config.py               # Configuration settings
├── requirements.txt        # Project dependencies
└── run.py                 # Application entry point


### Design Choices

1. **SQLite Database**
   - Chose SQLite for its simplicity and portability
   - No need for a separate database server
   - Suitable for single-user deployment

2. **Blueprint Structure**
   - Organized routes using blueprints for modularity
   - Separates concerns for better maintainability
   - Allows for future feature expansion

3. **File Upload Handling**
   - Implemented secure filename generation
   - Created separate upload directory
   - Added file type validation

4. **User Interface**
   - Clean, intuitive design
   - Mobile-responsive layout
   - Consistent color scheme and styling
   - Easy navigation between features

### Security Considerations

- Password hashing using Werkzeug's security functions
- CSRF protection on all forms
- Secure file upload handling
- User session management
- Data isolation between users

### Future Improvements

1. **Enhanced Features**
   - Email notifications for appointments
   - Data export functionality
   - Sharing capabilities with healthcare providers
   - More detailed pregnancy information

2. **Technical Enhancements**
   - Add unit tests
   - Implement caching
   - Add API endpoints
   - Enhanced error handling

3. **User Experience**
   - More interactive dashboards
   - Data visualization improvements
   - Customizable tracking options
   - Multi-language support

### Installation and Setup

1. Clone the repository
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Set up environment variables
5. Initialize the database: `flask db upgrade`
6. Run the application: `python run.py`

### Author
[Austin Ben Simiyu]

### Acknowledgments
- CS50 staff for the excellent course content
- Flask documentation and community
- Bootstrap for UI components