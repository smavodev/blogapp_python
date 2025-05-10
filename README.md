# Python

## Crear entorno virtual para el proyecto
```python -m venv venv```

### Backup de librerias instaladas
```pip freeze > requirements.txt```

### Instalaciones previas
```pip install -r requirements.txt```

### Desinstalar de manera masiva librerias
```pip uninstall -r requirements.txt -y```

## Subir las migraciones a la base de datos
```python manage.py makemigrations```

```python manage.py showmigrations```

```python manage.py migrate```

### Crear usuario administrador
```python manage.py createsuperuser```

### Iniciar el servidor con Django
```python manage.py runserver```

### Add Dumpdata 
```python manage.py dumpdata > blogapp.json```

### Load Dumpdata
```python manage.py loaddata blogapp.json```

### Importante:
Una vez clonado el repositorio asegurate de primero crear la base de datos antes de levantar el proyecto.
- Instalar dependencias
- Registrar BD (Postgresql)
- Correr las migraciones
- Levantar el proyecto en local

### Acceso Admin
http://127.0.0.1:8000/admin_blogapp/
Usuario: smavodev
Password: 1nd1.sm4rT%%

### Usuarios
http://127.0.0.1:8000/accounts/login/
Usuario: yadirasa, smavotest, sergio
Password: 1nd1.sm4rT%%
