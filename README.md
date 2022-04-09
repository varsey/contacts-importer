# contacts-importer
Django project. Imports contact info line by line from csv file

### Development


Create a virtualenv using Python 3 and install dependencies. I recommend getting python3 using a package manager (homebrew on OSX), then installing [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation) to that python. NOTE! You must change 'path/to/python3'
to be the actual path to python3 on your system.

    mkvirtualenv contacts_importer --python=/path/to/python3
    pip install -r requirements.txt

Set up db:

    python manage.py migrate

Run server:

    python manage.py runserver


For tests: binary chrome driver for test (to be unpacked to env/bin dir):
- wget https://chromedriver.storage.googleapis.com/100.0.4896.20/chromedriver_linux64.zip
