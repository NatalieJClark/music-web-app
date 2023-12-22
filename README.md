# Music Web App

## Introduction

- This is my web music app project for Makers Module 4 - Web Applications: Flask routes
- It is a database-backed web app that stores artists and albums
- It includes a coach assessed challenge (See objectives below)

## Objectives

I used this project to:
- [x] Consolidate how to set up a Flask project
- [x] Consolidate how to design a single table schema from a specification
- [x] Consolidate how to build routes from a specification
- [x] Learn how to test-drive routes with a database

Test Drive Routes with Databases Challenge:
- [x] Test-drive a route GET /artists, which returns the list of artists:
```shell
# Request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone
```
- [x] Test-drive a route POST /artists, which creates a new artist in the database.
- [x] Your test should verify the new artist is returned in the response of GET /artists.
```shell
# Request:
POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)
(No content)

# Then subsequent request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing
```

## Setup
```shell
# Clone the repository to your local machine
; git clone https://github.com/NatalieJClark/music-web-app.git YOUR_PROJECT_NAME

# Enter the directory
; cd YOUR_PROJECT_NAME

# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell

# Create a test and development database
; createdb YOUR_PROJECT_NAME
; createdb YOUR_PROJECT_NAME_test

# Open lib/database_connection.py and change the database names
; open lib/database_connection.py

# Seed the development database (ensure you have run `pipenv shell` first)
; python seed_dev_database.py

# Run the tests (with extra logging)
; pytest -sv 

# Run the web server
; python app.py
# Now visit http://localhost:5001/albums or http://localhost:5001/artists in your browser
```

