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

In the settings.py of myproject:
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

**Note:** follow naming conventions. Config is always a capital C.
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

# Admin Page Setup
# Editing Views

