# Python

## Crear entorno virtual para el proyecto
```python -m venv venv```

## Instalaciones previas
```pip install -r requirements.txt```

## Subir las migraciones a la base de datos
```python manage.py makemigrations```

```python manage.py showmigrations```

```python manage.py migrate```

## Crear usuario administrador
```python manage.py createsuperuser```

## Iniciar el servidor con Django
```python manage.py runserver```


## Load Dumpdata
```python manage.py loaddata blog_app.json```