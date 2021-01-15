# Online Decision in Principle - The Initial Enquiry

This application represents a phase 1 offering of an initial enquiry to a Decision in Principle, to be filled in by a member of the public in order to be contacted by telephone by a mortgage adviser.

## Installation

It is assumed that you have the source code downloaded and have a cmd prompt open, currently residing in the root folder (where this readme file is located).

1. Create a virtual environment

```python 
python -m venv .
```

2. Activate the environment by typing the command:

```python
scripts\activate
```

3. Install the dependencies, there is an up to date requirements file, run the following cmd:

```python
pip install -r requirements.txt
```

## Before Running

A database has been provided with sample data to work from. There are several features that can be adjusted within the settings. Detailed below:

### Email

Upon submission of the enquiry form, the system can generate an email confirmation that will be sent to the email address provided by the user.
This functionality is disabled by default but can be activated by setting the following setting contained withing settings.py:

```python
ENABLE_EMAIL = True
```

If this setting is enabled then environment variables must be provided with the following names in order to utilise an email account:

```python
DJANGO_DEFAULT_FROM_EMAIL
DJANGO_EMAIL_HOST
DJANGO_EMAIL_HOST_PASSWORD
DJANGO_EMAIL_HOST_USER
DJANGO_EMAIL_PORT
```

SSL is enabled by default but can be disabled by changing the setting EMAIL_USE_SSL

### Maximum LTV

The Maximum Loan to Value (LTV) can be set within the ettings.py with the following variable:

```python
MAX_LTV
```

This value must be set between 0 and 100.

### Database info

There is an existing database with sample data and a default superuser set up already for convenience and testing purposes. The account details are below:

> username: admin
>
> password: admin

This account merely serves as a convenient method to access the database and set up a new superuser account. This account should be deleted before deploying the application.

## Running the Server

Once all settings have been adjusted to requirements, then move into the online_dip directory and use this command to run the server:

```python
python manage.py runserver
```

Different areas of the application can be accessed by visiting the following locations:

- http://127.0.0.1:8000/yourdetails/ - Head here to view the enquiry form. This is the part of the site that the public would see and use
- http://127.0.0.1:8000/adviser/enquiries - This area requires an account. There is no functionality to "register" for security purposes. You will need to create a new account in order to access this area
- http://127.0.0.1:8000/odip_admin/ - Is the admin area of the site. This is where you can create a new account and use the superuser details above to access.

## Testing

The application contains a vairety of tests. Some Selenium based, as such they can be quite slow to run, so they can be excluded. 

In order to run the selenium tests, you will need to download the ChromeDriver. This should be placed in the virtual environment folder you created earlier.

1. Ensure you are in the online_dip directory (where the manage.py file is located)... Start the server:

```python
python manage.py runserver
```

2. Open a second terminal (you may need to re-enter the environment variables detailed above) and run the command:

python manage.py test

This will run all of the tests. As mentioned earlier these can be skipped because they're tagged. In order to skip selenium tests, use the tag "fast". You can run either of the following:

```python
python manage.py test --tag=fast # Skip selenium tests
pythong manage.py test --tag=slow # To run ONLY selenium tests
```

### Links

- https://www.python.org/downloads/ - Python
- https://chromedriver.chromium.org/downloads - ChromeDriver