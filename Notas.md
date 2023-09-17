
# Python

## Instalaciones del Proyecto 

### Instalar DJANGO
```pip install django```

### Actualizar pip
```python.exe -m pip install --upgrade pip```

### Instalar Django en el proyecto
```django-admin startproject blogapp .```

### Crear app 'app'
```python manage.py startapp app```

### Instalar Pillow
```pip install Pillow```

### Crear las migraciones 
```python manage.py makemigrations```

### Ver las migraciones 
```python manage.py showmigrations```

### Agregar las migraciones al proyecto
```python manage.py migrate```

### Crear usuario administrador
```python manage.py createsuperuser```

### Cambiar password de usuario
```python manage.py changepassword <your_user_name>```

### Instalar django-ckeditor : 
https://github.com/django-ckeditor/django-ckeditor
https://pypi.org/project/django-ckeditor/#installation
```pip install django-ckeditor```

```
CKEDITOR_CONFIGS = {
    'default': {
        # 'toolbar': 'full',
        'toolbar': 'Basic',
        # 'height': 300,
        # 'width': 300,
    },
}

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]
    }
}
```

### Ejemplos de Paginacion
**https://stackoverflow.com/questions/30864011/display-only-some-of-the-page-numbers-by-django-pagination**

```
{% if all_posts.has_other_pages %}
	<ul class="pagination">
		{% if all_posts.has_previous %}
			<li class="page-item"><a class="page-link" href="?page={{all_posts.previous_page_number}}">Previous</a></li>
		{% else %}
			<li class="page-item disabled left-page"><a class="page-link" href="#">Previous</a></li>
		{% endif %}

		{% for i in all_posts.paginator.page_range %}
			{% if all_posts.number == i %}
				<li class="page-item active"><a class="page-link" href="#">{{i}}</a></li>
			{% else %}
				<li class="page-item"><a class="page-link" href="?page={{i}}">{{i}}</a></li>
			{% endif %}
		{% endfor %}

		{% if all_posts.has_next %}
			<li class="page-item"><a class="page-link" href="?page={{all_posts.next_page_number}}">Next</a></li>
		{% else %}
			<li class="page-item disabled right-page"><a class="page-link" href="#">Next</a></li>
		{% endif %}
	</ul>
{% endif %}
```


## Add django-admin-honeypot 
**https://pypi.org/project/django-admin-honeypot/**
```pip install django-admin-honeypot```
```pip install django-admin-honeypot-updated-2021``` # En caso salga error instalar esta versión


## Add Theme Jazzmin 
**https://django-jazzmin.readthedocs.io/configuration/**
```pip install django-jazzmin```


### Desactivar Jassmin y flujo basico
```
# 'jazzmin',
# LOGOUT_REDIRECT_URL = '/accounts/login'
```

## Add Requierements 
pip freeze > requirements.txt

## Add Dumpdata 
```python manage.py dumpdata > blog_app.json```


## Add python-decouple
* https://pypi.org/project/python-decouple/
```pip install python-decouple```

## Add psycopg2
* https://pypi.org/project/psycopg2/
```pip install psycopg2```

## Update Database 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT')
    }
}
```

