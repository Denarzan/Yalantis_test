## Installation
1. Clone project
```bash
git clone https://github.com/Denarzan/Yalantis_test/tree/master
```

2. Install packages
```bash
pip install -r requirements.txt
```

3. Setting db
```bash
cd catalog
python manage.py makemigrations
python manage.py migrate
```

4. Run server
```bash
python manage.py runserver
```
5. View, post requests, search and filter
```bash
http://127.0.0.1:8000/
```

6.Detail view, delete and change attributes
```bash
http://127.0.0.1:8000/{id}/
```