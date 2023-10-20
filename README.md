# My Personal Blog Website.
* https://takbirs-blogs.onrender.com
* My first end-to-end fullstack application, of which I managed managed development, deployment, and production.


## Functionality
* In order to comment on blog posts, users must be registered/logged in to the website.
* Passwords are securely encoded with hashing and stored in a SQL Database.
* User authentication (managed by Flask Login) is employed.
* Only users with admin privileges may add, edit, and delete blog posts.
* Through the Contact page, users can send messages to me (the owner). Messages are sent to me via SMTP Email Client.
* (Production) WSGI server is setup with Gunicorn to run the Live Python Application on Render. PostgreSQL database is used for production.
* (Development) Development and testing is done locally with a SQLite database.

## Build

* Python + Flask Web Framework Backend
* JavaScript/HTML/CSS Bootstrap Frontend
* SQL Databases
* Object-Oriented Programming (OOP)
* Python Decorators (for user permissions)

## Packages
* See requirements.txt for all packages and dependencies used.
