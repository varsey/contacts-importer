# contacts-importer
Django project. Imports contact info line by line from csv file

### Development


Install dependencies

    pip install -r requirements.txt

Set up db:

    python manage.py migrate

Run server:

    python manage.py runserver


For tests: binary chrome driver for test (to be unpacked to env/bin dir):
- wget https://chromedriver.storage.googleapis.com/100.0.4896.20/chromedriver_linux64.zip

Sample file to try:
 1) sample_files/sample-1.csv - normal file for default upload
 2) sample_files/sample-2.csv - file for upload with Date of Birth in 1st column and Name in 2nd.
    use selectors and "save settings" button before upload
 3) sample_files/sample-3.csv - special characters in name and empty fields in file, see summary for errors