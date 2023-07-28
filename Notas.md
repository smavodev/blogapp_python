
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