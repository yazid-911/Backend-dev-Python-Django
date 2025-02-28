# Recrutement Platform - Backend  

## Description  
Backend de la plateforme de recrutement, développé avec Django et Django REST Framework. Cette API expose des endpoints pour gérer les informations des candidats et des recruteurs.  

## Prérequis  
- Python  3.11
- PostgreSQL  
- pip  

## Installation  

1. **Clonez le dépôt** :   
$git clone https://github.com/yazid-911/Backend-dev-Python-Django 
$cd recrutement_backend

2. **Créez un environnement virtuel** :
$python -m venv venv  
$source venv/bin/activate  # Sur Unix/Mac  
$venv\Scripts\activate     # Sur Windows  

3. **Installez les dépendances** :
$pip install django djangorestframework psycopg2  

4. **Configurer PostgreSQL** :
Créez une base de données pour le projet.
Mettez à jour les paramètres de la base de données dans settings.py.

5. **Effectuer les migrations** :
$python manage.py migrate  

6. **Lancer le serveur de développement** :
$python manage.py runserver

7. **Accéder à l'API** :
L'API sera disponible sur http://127.0.0.1:8000/api/.
La documentation de l'API est générée avec Swagger et est accessible à http://127.0.0.1:8000/swagger/schema et avec redoc à http://127.0.0.1:8000/swagger/redoc


