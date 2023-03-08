# Simple_Django_Newsletter_App

The Django app offers a comprehensive solution for managing multiple mass-mailing lists. It allows you to create both plain text and HTML templates 
with integrated rich text widgets, and features a sophisticated queueing system, all manageable from the user-friendly admin interface.

## Features

- User registration and login system
- Ability to add, update, and delete articles
- Ability to add comments to articles
- Password reset functionality
- Newsletter management system
- Support for both plain text and HTML templates with rich text widgets
- Queueing system for sending mass emails
- User-friendly admin interface
- Built with Django, HTML, Bootstrap, and PostgreSQL

## Installation

- Clone this repository using git clone https://github.com/msdot001/News_Django.git
- Navigate to the cloned directory using cd news
- Create a new virtual environment using python -m venv env
- Activate the virtual environment using source env/bin/activate (Linux/Mac) or .\env\Scripts\activate (Windows)
- Install the dependencies using pip install -r requirements.txt
- Run the migrations using python manage.py migrate
- Create a superuser using python manage.py createsuperuser
- Run the development server using python manage.py runserver
- Open your browser and navigate to http://localhost:8000/admin to access the admin interface
- Use the admin interface to create newsletter templates, mailing lists, and subscribers
- Navigate to http://localhost:8000 to access the user-facing part of the app

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please open an issue or submit a pull request.
 
## License 
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). 
