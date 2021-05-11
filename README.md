# Business Website
Business website in Django

LINK: https://zeusgym.herokuapp.com

## Getting started
### Requirements
 - Python 3.6+
 - PIP
 - venv (Optional)

### Installation
```
# Clone the repository
git clone https://github.com/OmGDahale/business-website.git

# Enter into the directory
cd business-website/

# Create virtual environment (Optional)
python3 -m venv .venv

# Activate virtual environment (Optional)
source .venv/bin/activate

# Install the dependencies
pip install -r requirements.txt

# Apply migrations.
python manage.py migrate
```
### Configuration
Create `.env` file in cwd and add the following
```
SECRET_KEY=your_secret_key
DEBUG=True
EMAIL_USER=your_email_address
EMAIL_PASS=your_password
```
```
# Create a superuser account (follow the prompts afterwards)
python manage.py createsuperuser
```
### Starting the application
```
python manage.py runserver
```
