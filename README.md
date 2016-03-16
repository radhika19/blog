**BLOG**
>Blog repo is a working example of a blogging website (only APIs included).commenting w.r.t paragraph

**Installation:**

- setup the repo and install required modules from requirements.txt
```
git clone https://github.com/radhika19/blog.git
cd blog
```
when using virtualenv 
```
virtualenv .
. bin/activate
pip install -r requirements.txt
```
- to create an mysql server:
```
sudo apt-get install mysql-server
```
- the mysql database settings have been added in settings.py file. make changes w.r.t **user** and **password**
```
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': BLOG,
    'USER': <username>,
    'PASSWORD': <password>,
    'HOST': 'localhost',
    }
}
```
- migrate the models:
```
cd blog_project
python manage.py makemigrations blog_app
python manage.py migrate
```
- start the server
```
python manage.py runserver
```
- Note:To create the username/password for admin page. This page is just for view purpose.
```
 python manage.py createsuperuser
 ```
**API Reference:**

The APIs are documented with examples: [API document](https://github.com/radhika19/blog/blob/master/apiary.apib)

