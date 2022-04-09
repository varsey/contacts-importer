# contacts-importer
Django project. Imports contact info line by line from csv file

### Instructions


    git clone https://github.com/varsey/contacts-importer

 
_

    cd contacts-importer/
_
   
    python3 -m venv .
 _


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
    use selectors and "save settings" (select "2" for  Name and "1" for Date of Birth) button before upload
 3) sample_files/sample-3.csv - special characters in name and empty fields in file, see summary for errors

See logs for errors and number of records saved

Click "Clear records" to empty database and then "Run import in background" button for scheduling import from file every 5 secs

Run command (in separate console, activate venv if needed) - do nnothing and in 30 secs data is gonna be imported from sample_files/sample-1.csv

    python manage.py process_tasks


Update http://127.0.0.1:8000/contacts/ page in 5 secs to see data imported