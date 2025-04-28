Weather Project with Django
Project Overview
Goal: Build a Django web app that allows users to enter a city name and view current weather details (temperature, description, humidity, etc.).
Tools:
Django (backend framework)
OpenWeatherMap API (free tier for weather data)
HTML/CSS for frontend (Bootstrap for styling)
Python requests library for API calls
Features:
Input form for city name

Set Up the Django Project
Install Python and Django: Ensure Python is installed. Install Django and the requests library:
pip install django requests


Create a Django Project:
django-admin startproject weather_project
cd weather_project


Create a Django App:
python manage.py startapp weather

Get an OpenWeatherMap API Key
Sign up at OpenWeatherMap and get a free API key.
Store the API key securely (e.g., in environment variables or a .env file). For simplicity, we’ll add it directly in the code for this example, but use python-dotenv in production.

Run the Project
Apply Migrations:
python manage.py makemigrations
python manage.py migrate


Start the Development Server:
python manage.py runserver
Test the App: Open http://127.0.0.1:8000/ in your browser. Enter a city (e.g., "London") and submit to see the weather data.
