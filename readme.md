## connect postgresql
```bash
psql -U postgres
\c
```

# Commands to remember
    1. python manage.py runserver : For running the server
    2. python manage.py makemigration : To check migrations
    3. python manage.py migrate: To do the migrations
    4. python manage.py createsuperuser: To get username and password for adming panel of django
    5. python manage.py collectstatic: To collect all the static files
    6. python manage.py startapp <app_name>: To create an app 

# Steps

 ## 1. Setting up database to django(Postgresql): 
    -  Create a database in PGadmin of postgresql: In this case it is lcotubers. 
    -  Go to settings.py --> DATABASES
    -  Changes made: 


``` python
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lcotubers',
        'USER': 'postgres', 
        'PASSWORD': 'manas1316',
        'HOST': 'localhost'
```

    - NAME: name of the database
    - USER: owner of the database, usually postgres
    - PASSWORD: master password to login into database
    - HOST: for build it is localhost

    - Install psycopg2. 

## 2. Changing Djang-Admin Theme
    - install "djangocms_admin_style"
    - configure it by adding "djangocms_admin_style" to your INSTALLED_APPS just before 'django.contrib.admin'
    - run python manage.py migrate djangocms_admin_style
    - Create a folder in the root file of tubers, named "templates": To manage all the templates from outside. 
    - Go to settings.py -> Templates
    - under DIRS, write the name of the template folder, in our case it is "templates"

## 3. Configuring static files
    - create a folder in "tubers"(not root folder) named "static", so we can serve all the css, js files and images from here. 
    - Go to the bottom of settings.py 
    - Write this command: 

``` python
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'tubers/static')
    ]
```
    - import os, on the top of the settings.py
    - Run "python manage.py collectstatic" to collect all the static files. 

> We have to mention every app that is coming from anywhere in the 'INSTALLED_APPS' of settings.py

## 4. Creating apps
    - run: 
``` python
python manage.py startapp webpages
```
    - create a urls.py file in webpages.
    - The name of the app is given in the "apps.py" of the webpages, copy it: in our case it is WebpagesConfig
    - Go to settings.py of tubers. 
    - Under 'INSTALLED APPS', mention this
``` python
'webpages.apps.WebpagesConfig',
```

## 5. Setting urls.py of tubers
    - At first, we have to import something
``` python
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
```
    - under urlpatters: 
``` python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webpages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```
    - path('admin/', admin.site.urls) are already given in urls.py, which serve admin url. 
    - we have to add a url for homepage, and we use include because we want it to controlled by someone else, which is url of webpages('webpages.urls') in our case. 
    - then we concatenate urlpatters to static because we have to configure static files in urls.py too, which is gonna be same for every project.

## 6. Setting up urls.py of webpages
    - we are gonna handle the 'homepage, aboutpage, services and contact page' from here. 
``` python
from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('contact', views.contact, name="contact"),
]

```
    - we have to import the path from django.urls, so that we can creae urls. 
    - Then, import everything from views.py, because every function is being defined in views.py
    - under "urlpatters", we configure all the routes we want in our website('about'), and from where it is being served(views.about), then write a unique name of the route, which should be similar the route name(name="about")
    - Go to views.py, so that we can create functions for these routes. 
    - under views.py: 
``` python
from django.shortcuts import render

def home(request):
    pass

def about(request):
    pass

def services(request):
    pass

def contact(request):
    pass
```
    - Right now, we are not passing anything inside these functions. 

## 7. Making the routes alive by adding content in the routes. 
    - create a folder inside templates: As we mentioned in settings.py that all the static files are being served from templates folder.
    - create a "base.html" file too inside the templates, which will serve as a global html page. 
    - Under webpages folder of templates, create the html pages of all the routes: in our case, it is about, contact, home and service.
    - under "base.html" add: 
``` html
<h1>This is navbar</h1>

{% block content %}


{% endblock %}


<h1>This is fotter</h1>
<p>Coyright something</p>

```
    - This file is gonna serve as a global file, because if we change anything here, it will make changes to evry other html files too. 
    - Whatever we add between "block content" and "endblock", it will be written in between the both th h1 tags. 
    - under about.html add: 
``` html 
{% extends 'base.html' %}

{% block content %}

<h1>About Us</h1>

{% endblock %}
```
    - Here, we are extending 'base.html", so that it can serve this file as base file, and we are writing all the tags inside the block content so that it will come in between navbar and footer of the base.html.
    - Follow the same syntax to every other html page.

> Whener we are working with some static html files, then at the top we have to mention {% load static %}

## 8. Working with static html files: base.html

> One bug that we will be facing for loading the static files is that, the html files are going to be inside the templates, but all the css, js and images are going to be inside the static files, in the root folder. 

> The best way to load your css, js and images is to put {% load static %} at the top of the html page and then everywhere at css, js and images src part of the html, convert basic './css/style.css' to

``` python
    {% static './css/style.css' %}
```

## 9. Creating Components
    - At first, we added everything in base.html, including header, footer and even script files. But, when as a professional developer, we have to seperate it out to make our code look simple, so that later we can modify and find the bugs easily. 

    - Create a folder inside the template folde( in our case,  it is includes ), and create different html files as componenent, one for header, one for navbar, other for footer etc and include the code of that part inside it. 

    - If that part of code includes static file, then we have to load it on the top first. 

    - To load the component, we have to include that component in the main file( in our case it is base.html ) by using this code: 
``` python 
    {% include 'includes/<file_name>.html' %}
```

## 10.  Creating Model for Slider
    a. Now, we have to create a model for slider, with the help of which we can add data from admin. 

    b. Add this code to models.py of webpages folder. 
``` python
class Slider(models.Model):
    headline = models.CharField(max_length = 255)
    subtitle = models.CharField(max_length = 255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/slider/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)
```
    c. Now, register this Slider class in admin.py of webpages, to be recognized by admin page. 
``` python
from .models import Slider

admin.site.register(Slider)
```

> To change the default name of the saved slider in admin, you have to overwrite the __str__ function of the python in models.py under Slider class. 
```python 
def __str__(self):
    return self.headline
```

## 11. Pulling data from Admin Panel to the home page
    a. Move to views.py of webpages folder
    b. import Slider from models by adding: 
```python
from .models import Slider
```
    c. We have to put this slider inside home, so we will add this feature inside home function of views.py

    d. Add these lines in home function on top: 
```python
sliders = Slider.objects.all()
data = {
    'sliders': sliders
}
```
    e. objects is making queries and adding all in it, means that we want to extract everything that is present in Slider.

    f. After declaring sliders variables, you should have to put that variable inside data. 

    g. After all this, you want your data to be rendered with home, and for that, you have to clip third part of the return part of home function as "data"
```python 
return render(request, 'webpages/home.html', data)
```

> Whenever we want to add a variable inside the django as jinja template, then instead of {%  %},  we should use {{  }}