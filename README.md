Meditation Website
This Django project is a full-fledged website designed to provide meditation and mental wellness exercises. It includes features for user registration, login, and access to various meditation sessions.

Project Features
User Registration: Users can create a new account to access the site's features.

User Login: Existing users can log in securely.

Meditation Sessions: The platform provides access to a variety of guided meditation sessions.

Email Notifications: Future plans include adding functionality for sending notifications to users about new sessions.

Secure Password Handling: Passwords are handled securely using Django's built-in authentication system.

Prerequisites
To run this project on your local machine, you need to have the following software installed:

Python 3.13+

pip

Git

Local Installation and Running
Follow these steps to get the project up and running on your local machine.

1. Clone the Repository:

Use Git to clone this repository to your local machine.

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Create a Virtual Environment:

It is best practice to use a virtual environment to manage dependencies.

python -m venv .venv

3. Activate the Virtual Environment:

Windows:

.venv\Scripts\activate

macOS / Linux:

source .venv/bin/activate

4. Install Dependencies:

Install all the required dependencies from the requirements.txt file.

pip install -r requirements.txt

5. Apply Database Migrations:

Run the migrations to set up the database structure.

python manage.py makemigrations
python manage.py migrate

6. Run the Development Server:

Now you can start the Django development server.

python manage.py runserver

Your website will be accessible at http://127.0.0.1:8000/.

How to Deploy
To deploy this project on a platform like Render, you will need the following files and changes:

requirements.txt: Generate this file by running pip freeze > requirements.txt.

Procfile: Create a file named Procfile in the same directory as manage.py with the content web: gunicorn myproject.wsgi.

settings.py: Set DEBUG = False and add your production URL to ALLOWED_HOSTS. Using environment variables for sensitive data like SECRET_KEY is highly recommended for production.

Contributions
If you would like to contribute to this project, please feel free to send a pull request or open an issue.

License
This project is licensed under the MIT License.