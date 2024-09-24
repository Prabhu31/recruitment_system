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

# API Endpoints

## List All Candidates
- **URL**: `/candidates/`
- **Method**: `GET`
- **Description**: Retrieves a list of all candidates.

## Create a New Candidate
- **URL**: `/candidates/`
- **Method**: `POST`
- **Description**: Adds a new candidate to the system.
- **Required Fields**: `name`, `age`, `gender`, `email`, `phone_number`

## Retrieve a Specific Candidate
- **URL**: `/candidates/{id}/`
- **Method**: `GET`
- **Description**: Gets details of a candidate by their ID.

## Update a Candidate's Information
- **URL**: `/candidates/{id}/`
- **Method**: `PUT` or `PATCH`
- **Description**: Updates the details of an existing candidate.

## Delete a Candidate
- **URL**: `/candidates/{id}/`
- **Method**: `DELETE`
- **Description**: Removes a candidate from the system.

## Search Candidates
- **URL**: `/candidates/search/`
- **Method**: `GET`
- **Description**: Search for candidates by name using a query parameter.
- **Query Parameter**: `q` - Search term to find candidates by name.