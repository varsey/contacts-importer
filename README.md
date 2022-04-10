# contacts-importer
Django project. Imports contact info line by line from csv file

### Instructions
Clone project

    git clone https://github.com/varsey/contacts-importer

Go to project directory

    cd contacts-importer/
Create virtual environment
   
    python3 -m venv .
Activate virtual enviroment


    source ./bin/activate

 
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
    Use selectors (select "2" for  Name and "1" for Date of Birth) and hit "save settings"  button before upload
 3) sample_files/sample-3.csv - special characters in name and empty fields in file, see summary for errors

Click "Clear records" to empty database and then "Run import in background" button for scheduling import from file every 30 secs

Run command (in separate console, activate venv if needed) - do nothing and in 30 secs data is gonna be imported from sample_files/sample-1.csv, just refresh page to see

    python manage.py process_tasks


Update http://127.0.0.1:8000/contacts/ page in 30 secs to see data imported