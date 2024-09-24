Recruitment System

Overview:
This is a Django-based recruitment system for managing candidates.

Requirements:
- Python 3.x
- Django
- Django REST Framework

Setup Instructions:

1. Clone the repository:
   git clone git@github.com:Prabhu31/recruitment_system.git
   
   cd recruitment_system

3. Create a virtual environment:
   python -m venv venv

4. Activate the virtual environment:
   - On Windows: venv\Scripts\activate
   - On macOS/Linux: source venv/bin/activate

5. Install the requirements:
   pip install -r requirements.txt

6. Run migrations:
   python manage.py migrate

7. Create a superuser:
   python manage.py createsuperuser

8. Run the development server:
   python manage.py runserver

9. Access the admin panel:
   Open your web browser and go to http://127.0.0.1:8000/admin/ to log in with your superuser credentials.
