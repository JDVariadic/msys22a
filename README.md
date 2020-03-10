### Code for MSYS22A
## Instructions:

# Classroom laptops:
Retrieve your file and place it in your folder.
Run the command

```
\msys22[id#]\Scripts\activate
```

on the directory named by your id number.

Then, code normally.

# Own Laptop:

**Note:** If the only time you installed python was from Anaconda, I suggest you uninstall that and do a fresh python install.

Install Python: https://www.python.org/downloads/

Install Pip on Command Prompt (Package Manager):

```
python get-pip.py
```

Test if you actually have it:

```
pip -V
```

Then, begin creating the project/app normally.

## Cheatsheet: 
# Web-App General setup
```
django-admin startproject myproject
python manage.py startapp myapp
```

In the **settings.py** of myproject:
Edit, (For this example, im using the name myapp)
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp.apps.myappConfig', 
]
```

*Note:* follow naming conventions. Config is always a capital C.

**REQUIRED:** Change allowed hosts using

```
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
```

and create a new variable after STATIC_URL by

```
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

**OPTIONAL** Change timezones in 
```
TIME_ZONE = 'PST'
USE_TZ = True
```
# Introduction to the MVC Model

# Running the Server

```
python manage.py runserver
```

# Admin Page Setup
```
python manage.py createsuperuser
```

# Creating Models
Under the app directory, go to models.py
Sample Code:
```
class Supplier(models.Model):
    name = models.CharField(max_length = 300)
    city = models.CharField(max_length = 300)
    country = models.CharField(max_length = 300)
    created_at = models.DateTimeField(blank = True, null = True)
    objects = models.Manager()

    def __str__(self):
      return str(self.pk) + ': ' + self.name + ', ' + self.city + ', ' + self.country + ', ' + str(self.created_at)
```
```models.Model``` Tells python that the class is of type model
```CharField``` and ```DateTimeField``` signify the data types of the fields. For more field types, you can go to: https://docs.djangoproject.com/en/3.0/ref/models/fields/

# Adding Models to Admin Page
When to **migrate**:
Typical rule of thumb is to
```
python manage.py makemigrations
```
and
```
python manage.py migrate
```

When editing code that refers to **adding** into the database
Examples: Editing Field types, Adding new variables

No need to migrate when editing code that refers to **viewing** the database.
Examples: editing the str function of a class.

(Note: Not an end all be all rule)

# Editing Views

