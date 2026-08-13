# Instagram Clone

## 📌 About the Project

Instagram Clone is a full-stack social media web application inspired by the core concept and user experience of Instagram.

The project is being developed using **Django** as the backend framework, with the goal of building a complete social media platform from the ground up while understanding how a real-world web application is designed, structured, and developed.

Rather than simply creating a static interface, this project focuses on implementing the backend architecture and functionality required for a social media application, including user management, authentication, sessions, database interactions, request handling, forms, templates, and access control.

The application is being developed incrementally, with different parts of the system being added and improved as development progresses.

---

## 🎯 Why This Project Was Created

This project was created primarily as a **Django backend learning and practical development project**.

Instead of learning Django concepts independently through small examples, the goal is to understand how those concepts work together inside a real application.

The project provides practical experience with:

- Building a Django project from scratch
- Structuring applications using Django apps
- Designing backend logic
- Working with databases and models
- Handling user authentication
- Managing sessions
- Processing forms and requests
- Protecting authenticated resources
- Connecting frontend templates with backend logic
- Organizing static files and project resources
- Following a maintainable project structure

The long-term goal is to continue expanding the project into a more complete social media platform while using it as a practical way to strengthen backend development skills.

---

## 🛠️ Technology Stack

### Backend

- **Python**
- **Django**

Django is used as the primary backend framework responsible for request handling, authentication, database interaction, URL routing, forms, sessions, and application logic.

### Frontend

- **HTML**
- **CSS**
- **Django Templates**

Django's template system is used to connect the frontend interface with backend data and logic.

### Database

- **SQLite**

SQLite is currently used as the development database because it is lightweight and convenient during development.

### Development Tools

- **Git**
- **GitHub**
- **Visual Studio Code**

Git is used for version control, while GitHub is used to host and manage the project repository.

---

## 🏗️ Project Architecture

The project follows Django's application-based architecture.

Instead of putting the entire application inside one large Django app, functionality is divided into separate applications based on responsibility.

For example:

```text
instagram_clone/
│
├── accounts/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── signals.py
│   ├── templates/
│   └── static/
│
├── home/
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── static/
│
├── instagram_clone/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
├── .gitignore
└── README.md
```

The application is designed so that different responsibilities can be separated into their own Django apps as the project grows.

This makes the project easier to maintain, understand, test, and expand.

---

## 🔐 Authentication and User Management

The project uses Django's built-in authentication system to handle user authentication.

The authentication architecture includes:

```text
User
  ↓
Signup
  ↓
User Creation
  ↓
Authentication
  ↓
Session
  ↓
Authenticated Requests
  ↓
Protected Resources
```

Django's authentication system is used instead of implementing authentication manually.

The project also makes use of Django's session system to maintain authentication state between HTTP requests.

---

## 🔄 Request and Response Architecture

The application follows Django's request-response architecture.

A simplified flow is:

```text
Browser
   ↓
HTTP Request
   ↓
Django URL Resolver
   ↓
View
   ↓
Business Logic
   ↓
Database / Forms / Authentication
   ↓
Template
   ↓
HTTP Response
   ↓
Browser
```

This project provides practical experience with both **GET and POST requests**, form processing, redirects, sessions, and Django's template rendering system.

---

## 📚 Learning Objectives

The main objective of this project is to develop a deeper understanding of backend development through practical implementation.

The project is helping build experience with:

- Django architecture
- Backend development
- Authentication systems
- Database-driven applications
- HTTP request/response cycles
- Sessions and state management
- Form validation
- Template rendering
- URL routing
- Access control
- Django signals
- Static files
- Git and GitHub
- Project organization

---

## 🚧 Project Status

**Currently under development.**

The application is being developed incrementally. The current implementation focuses on establishing the core Django architecture and authentication system.

Additional social media functionality will be introduced as development continues.

---

## 🔮 Future Development

The project is intended to gradually evolve into a more complete social media platform.

Future development may include areas such as:

- User profiles
- Posts and media uploads
- Following and followers
- Likes and comments
- Personalized feeds
- Search
- Notifications
- Messaging
- Profile customization
- Additional security and production features
- API development

These components will be implemented progressively as the project develops.

---

## 💻 Running the Project Locally

### Clone the repository

```bash
git clone <your-repository-url>
cd instagram_clone
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Apply database migrations

```bash
python manage.py migrate
```

### Start the development server

```bash
python manage.py runserver
```

The application will then be available at:

```text
http://127.0.0.1:8000/
```

---

## 👨‍💻 Author

**Shrishant Jadhav**

GitHub: [@shrishantjadhav](https://github.com/shrishantjadhav)

---

## 📄 License

This project is currently developed for educational and learning purposes.
