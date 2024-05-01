# Kiratech Backend Assignment

## Required packages
- Django
- Django Rest Framework

## Setup
- Make sure all packages are installed
- Run in cmd 
  - py manage.py makemigrations
  - py manage.py migrate
- Start the server by running
  - py manage.py runserver

**Note**: If I'm not wrong, there should be dummy data inserted in the database during my development. Please ignore the wacky names 😅

## Admin Panel Account details
- **Username**: admin
- **Password**: password

## To access Inventory
URLs below will access the main functions of the app
URL Query parameters are also implemented
- http://127.0.0.1:8000/inventory/
- http://127.0.0.1:8000/inventory/1
- http://127.0.0.1:8000/inventory/?name=The+item

## The API
URLs below will show DRF API View
This is the API that supplies the data to the inventory views above
- http://127.0.0.1:8000/api/inventory/
- http://127.0.0.1:8000/api/inventory/?name=The+item

## References
https://www.youtube.com/watch?v=i5JykvxUk_A

https://www.youtube.com/watch?v=sJRR7gz6B1E

https://stackoverflow.com/questions/47088201/rendering-templates-with-django-rest-framework

https://www.django-rest-framework.org/api-guide/renderers/#templatehtmlrenderer

https://www.w3schools.com/django/django_queryset_filter.php

https://www.youtube.com/watch?v=idhO5cLnkzk

https://www.geeksforgeeks.org/get_object_or_404-method-in-django-models/
