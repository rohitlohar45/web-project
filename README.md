1. Create Virtual Environment
```
python3 -m venv venv
```
2. Active Virtual Environment
```
source venv/bin/activate
```
3. Install Requirements File
```
pip install -r requirements.txt
```
4. Migrate Database
```
python manage.py migrate
```
5. Create Super User
```
python manage.py createsuperuser
```
6. Run Project
```
python manage.py runserver
```
