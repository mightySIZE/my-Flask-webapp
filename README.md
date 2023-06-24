# Goal
This project is meant for me to develope S/W engineering skills. I really like python and want to start learning Flask and Django first. Hence why this project. 

# Implementations thus far
1. login/signup/logout functionality
2. database integration with sqlite (SQLAlchemy and migrate)
3. Bycrypt for password hashing
4. login/user/session managment
5. forms for registeration and logining in
6. models for database
7. routes for db input and output
8. flashes for error handling
9. public API (cat facts 'https://alexwohlbruck.github.io/cat-facts/docs/')


# Libraries Used
	alembic==1.11.0 # this library is a database migration tool for SQLAlchemy
	flask==2.3.2 # this library is used to create the web application
	flask-migrate==2.4.0 # this library is used to manage database migrations, also uses Alembic
	flask-sqlalchemy==3.0.3 # this library is used to manage the database
	flask-wtf==1.1.1 # this library is used to work with wtforms and flask
	wtforms==3.0.1 # this library is used to create forms, such as the login form
	jinja2==3.1.2 # this library is used to create the templates
	sqlalchemy==2.0.13 # this library is used to work with the database
	sqlite==3.41.2 # this library is used to work with the database # I am using this in this application
	werkzeug==2.3.4 # provides a solid base for building web applications by offering essential functionalities like routing, request and response handling, URL generation, and more. flask is built on top of this library
	email_validator==2.0.0.post2 # this library is used to validate email addresses
	bcrypt==4.0.1 # this library is used to hash passwords
	flask_bcrypt==1.0.1 # this library is used to hash passwords in flask
	flask_login==0.6.2 # this library is used to manage the user login
	python-dotenv==1.0.0 # this library is used to load environment variables from a .env file
	requests=2.31.0 # this library is used to make HTTP requests
