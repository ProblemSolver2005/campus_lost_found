
# Campus Lost and Found Portal

A web application built using Django that helps students report lost and found items on campus.

Users can report lost or found items, upload images, search for items, and manage their own listings.

## Features

- User registration and login
- Report lost and found items
- Upload item images
- Search and filter items
- View item details
- Edit and delete listings
- Mark items as returned
- Django admin panel

## Technologies Used

- Python
- Django
- HTML
- CSS
- JavaScript
- SQLite

## Installation

1. Clone the repository:

   git clone YOUR_REPOSITORY_URL

2. Navigate to the project folder:

   cd campus_lost_found

3. Create a virtual environment:

   python -m venv venv

4. Activate the virtual environment:

   Windows:
   venv\Scripts\activate

   Linux/Mac:
   source venv/bin/activate

5. Install dependencies:

   pip install django pillow

6. Apply database migrations:

   python manage.py migrate

7. Create an admin account:

   python manage.py createsuperuser

8. Start the development server:

   python manage.py runserver

9. Open in your browser:

   http://127.0.0.1:8000/

## Admin Panel

http://127.0.0.1:8000/admin/

## Author

Your Name
