# News_test

Hacker News clone with RESTful API endpoints.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing


* Create a virtualenv for the project
* Install the requirements.txt file with pip


```
pip install -r requirements.txt
```
* Create Postgresql db corresponding to settings.py

* Run the django server

```
python ./manage.py runserver
```

* Enjoy the site at 127.0.0.1:8000 or your corresponding localhost

### Docker
* Change parameter in settings.py
```
DATABASES = {
    "default": {
        ...
        "HOST": "db",
        ...
    }
}
```
* Build with docker-compose

### Postman collection
```
https://www.getpostman.com/collections/baf5467cce196e1d6c07
```

### Heroku deployment
#### Website link
```
https://boiling-sea-64057.herokuapp.com/
```


#### Api endpoints
```
https://boiling-sea-64057.herokuapp.com/api/posts/
https://boiling-sea-64057.herokuapp.com/api/comments/
```
