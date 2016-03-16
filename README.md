**BLOG**
>Blog repo is a working example of a blogging website (only APIs included).commenting w.r.t paragraph

**Installation:**
>setup the repo and install required modules from requirements.txt
```
git clone https://github.com/radhika19/blog.git
cd blog
pip install -r requirements.txt
```
>to migrate the models to mysql database:
```
python manage.py makemigrations
python manage.py migrate
```
>start the server
```
python manage.py runserver
```
Note: python manage.py createsuperuser
     To create the username/password for admin page. This page is just for view purpose.

**API Reference:**

The APIs are documented with examples: [API document](https://github.com/radhika19/blog/blob/master/apiary.apib)

