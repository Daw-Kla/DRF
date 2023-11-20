# DRF
Django REST Framework app

This project is a simple visualisation of most popular Django REST API functionalities such as:
* creating a model instance in DB
* removing a model instance from DB
* updatnig a model instacne in DB
* taking single data of a object through API
* listing several objects from DB

## Technologies
Project is created with:
* Python 3.11
* django 4.2.0
* djangorestframework
* pyyaml
* requests
* django-cors-headers


## Set up a virtual enviroment in DRF directory

* for Windows:
```
python -m venv venv
```

* for Linux:
```
python3 -m venv venv
```

Then go to DRF/venv/Scripts and run:

```
.\activate
```
Go back to DRF directory and install requred libraries and packages

## Install requred libraries by runing:

* for Windows:
```
pip -r install requirements.txt
```

* for Linux:
```
pip3 install -r requirements.txt
```

# Project tree 

```
DRF 
├─ backend
│  ├─ api
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ models.py
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  ├─ cfehome
│  │  ├─ asgi.py
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  ├─ wsgi.py
│  ├─ manage.py
│  └─ products
│     ├─ admin.py
│     ├─ apps.py
│     ├─ forms.py
│     ├─ models.py
│     ├─ serializers.py
│     ├─ tests.py
│     ├─ urls.py
│     ├─ views.py
├─ LICENSE
├─ py_client
│  ├─ basic.py
│  ├─ create.py
│  ├─ delete.py
│  ├─ detail.py
│  ├─ list.py
│  ├─ not_found.py
│  ├─ update.py
├─ README.md
└─ reqiurements.txt

```