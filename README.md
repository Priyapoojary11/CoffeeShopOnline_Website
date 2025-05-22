# Coffee Shop Web Application ☕️

## Project Status 🚧

This project is currently a **work in progress**.  
Key features and enhancements are being actively developed, and updates will be committed regularly.  

---

### Planned Features:
- Enhanced user interface with additional styles and responsiveness.
- User profiles to track orders and preferences.
- Additional payment gateways for more flexibility.
- Automated deployment scripts.

---

**Django-based web application** for managing a coffee shop with user authentication, menu management, and payment integration.

---

## Features ✨

- **User Authentication**: Login, logout, and redirect mechanisms for users.
- **Menu Management**: 
  - View coffee items.
  - Add new items.
  - Edit or delete items.
- **Payment Integration**: Google Pay functionality using Stripe API.
- **Admin Panel**: Manage users and menu items with Django's built-in admin interface.
    - View coffee items.
    - Add new items.
    - Edit or delete items (admin only).

---

## Project Structure 📂

coffeeshop/ 

├── coffee/ 
    │ 
    ├── migrations/ # Database migrations 
    │ 
    ├── static/ # Static files (CSS, JavaScript, images) 
    │ 
    ├── templates/ # HTML templates for views 
    │ 
    ├── urls.py # URL routing for the app 
    │ 
    ├── views.py # View logic 
    │ 
    ├── models.py # Database models 
    │ 
    └── forms.py # Django forms for input handling 
    ├── coffeeshop/ 
    │ 
    ├── settings.py # Project settings 
    │ 
    ├── urls.py # Root URL configuration 
    │ 
    ├── wsgi.py # WSGI entry point 
    │ 
    └── asgi.py # ASGI entry point 
    ├── requirements.txt # Python dependencies 
    ├── manage.py # Django CLI 
    └── README.md # Project documentation

---

## Installation Instructions 🛠️

### Prerequisites:
- Python 3.9+
- Django 5.1
- Stripe account (for payment)

### Steps to Set Up:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Priyapoojary11/coffee-shop.git
   cd coffee-shop