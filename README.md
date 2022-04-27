# Test API for comment trees


## Local setup

### Versions
    Python 3.8
    Postgres 14.2
    Django 3.2.5

### Database
Create Postgres database called api_db
```
$ psql -U %username% postgres
# CREATE DATABASE api_db;
# \q
$ psql -U %username% api_db
```

### Set up virtual environment

```
cd ~/work/test_api_comment
python3 -m venv venv 
source venv/bin/activate 
pip3 install -r requirements.txt 
```

### Check if it works

```
cd ~/work/test_api_comment
./manage.py
```

### Migrate database

```
cd ~/work/test_api_comment 
./manage.py migrate
```

### Starts server
```
cd ~/work/test_api_comment
./manage.py runserver
```


