# Django REST API

Django REST API with Django Rest Framework

Example managing users and sending emails via SendGrid when a new user is created.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need Pip, Python and cURL packages installed

### Installing

Clone the project

```bash
git clone git@github.com:amalv/django-api.git
```

Create a virtual environment to isolate packages locally

```bash
python3 -m venv env
source env/bin/activate
```

Install Django and Django Rest Framework into the virtual environment

```bash
pip install django
pip install djangorestframework
pip install -U python-dotenv
```

Create database (SQLite by default)

```bash
python manage.py migrate
```

Create a super user

```bash
python manage.py createsuperuser --email admin@example.com --username admin
```

### Configuration

Create a `.env` file with the following config:

```bash
SENDGRID_API_KEY='<YOUR_SENDGRID_API_KEY>'
SENDER_EMAIL='<YOUR_SENDER_EMAIL>'
```

This will allow to send emails when a new user is added.

Don't forget to validate your sender email using [Single Sender Verification](https://sendgrid.com/docs/ui/sending-email/sender-verification/)

You can read the documentation about sending emails with Django and Sendgrid [here](https://www.twilio.com/blog/using-twilio-sendgrid-send-emails-python-django)

## Testing the API

Run the server

```bash
python manage.py runserver
```

Execute cURL request to get a list of users

```bash
curl -H 'Accept: application/json; indent=2' http://admin:<YOUR_ADMIN_PASSWORD>@127.0.0.1:8000/users/
```

You should see the following output

```json
[
  {
    "url": "http://127.0.0.1:8000/users/1/",
    "username": "admin",
    "first_name": "",
    "email": "admin@example.com"
  }
]
```

## Testing the API with a public URL

Sign up to ngrok and download the client for exposing your local webserver

[Download ngrok](https://ngrok.com/download)

Unzip to install

```bash
unzip /path/to/ngrok.zip
```

Connect to your account using the token
[token](https://dashboard.ngrok.com/auth/your-authtoken)

```bash
./ngrok authtoken <YOUR_AUTH_TOKEN>
```

Start HTTP tunnel on port 8000

```bash
./ngrok http 8000
```

Add the ngrok HOST in the `.env` file:

NGROK_HOST='<YOUR_NGROK_HOST>'

Execute cURL request to get a list of users

```bash
curl -H 'Accept: application/json; indent=2' https://admin:<YOUR_ADMIN_PASSWORD>@<NGROK_HOST>/users/
```

You should see the following output

```bash
[
  {
    "url": "http://<NGROK_URL>/users/1/",
    "username": "admin",
    "first_name": "",
    "email": "admin@example.com"
  }
]
```
