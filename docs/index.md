---
layout: default
title: Home
nav_order: 1
description: "Just the Docs is a responsive Jekyll theme with built-in search that is easily customizable and hosted on GitHub Pages."
permalink: /
---

# Incident Management System Documentation
{: .fs-9 }

An Incident Management System specialized for Elections.
{: .fs-6 .fw-300 }

[Get started now](#getting-started){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 } [View it on GitHub](https://github.com/ECLK/IncidentManagement){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## Getting started

### Dependencies

#### BACKEND
  - Language: Python
  - Framework: Django

#### FRONTEND 
  - Language: Javascript
  - Framework: ReactJS

### Quick start: Use Docker-Compose 

#### BACKEND
1. Make sure Docker is installed and running.
2. Navigate to `/backend` directory on terminal.
3. Build the docker image
```bash
$ docker-compose build
```
4. Create and run a new docker container instance.
```bash
$ docker-compose up
``` 
<small>At the very first run django will start before mysql by which will result an error for django to start. Stop (`ctrl + c`) and re-run.</small>
5. Open a new terminal (window/tab), navigate to `backend` folder
6. Run the migration to populate the data tables
```bash
$ docker-compose exec djangoapp python manage.py migrate
```
7. Create superuser account and enter information when prompted.
```bash
$ docker-compose exec djangoapp python manage.py createsuperuser
```
8. Run the seeder to populate data on the DB.
```bash
$ docker-compose exec djangoapp python manage.py loaddata category channel province district police politicalparty segment
```
9. In order to add predefined users, run users seeder.
```bash 
$ docker-compose exec djangoapp python manage.py loaddata users
```
<small>You may skip this step to implement you own user hierarchy.</small>
10. Server now runs at localhost on port 8000.


#### FRONTEND 
1. Make sure backend server is running.
2. Navigate to `/frontend` directory on terminal.
3. Build the docker image
```bash
$ docker-compose build
```
4. Create and run a new docker container instance.
```bash
$ docker-compose up
```

This is production build, thus not development friendly. For development purposes try [Local Installation](#local-installation). 


### Local installation: 

#### BACKEND
1. Make sure you have Python 3 and Mysql 8 installed. (for multiple versions you can use multiple environments with [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)).
2. Navigate to `/backend` directory on terminal.
3. Create new database and update database connection data on `/backend/src/settings.py` or `/backend/.env/` file.
3. Install all necessary python packages along with Django.
```bash
$ pip install -r requirements.txt
```
4. Run migrations for populate tables to DB.
```bash
$ python manage.py migate
```
5. Create superuser account and enter information when prompted.
```bash
$ docker-compose exec djangoapp python manage.py createsuperuser
```
6. Run the seeder to populate data on the DB.
```bash
$ docker-compose exec djangoapp python manage.py loaddata category channel province district police politicalparty segment
```
7. In order to add predefined users, run users seeder.
```bash 
$ docker-compose exec djangoapp python manage.py loaddata users
```
<small>You may skip this step to implement you own user hierarchy.</small>
8. Run the server locally on port 8000 and point your web browser to [http://localhost:8000](http://localhost:8000) to view swagger view for API implementation.
```bash
$ python manage.py runserver 0.0.0.0:8000
```
<small>Here you will now see only the public API list. You need to login on admin panel and visit back to baseurl (locally its: http://localhost:8000/) to see all API Endpoints</small>

Visit [http://localhost:8000/admin](http://localhost:8000/admin) and login using credentials of the superuser you created. 


### Configure Just the Docs

- [See configuration options]({{ site.baseurl }}{% link docs/configuration.md %})

---

## About the project

An Incident Management System specialized for Elections specifically designed for and managed by Election Commission of Sri Lanka.

### License

Incident Management System is distributed by an [MIT license](https://github.com/ECLK/IncidentManagement/blob/master/LICENSE.md).

### Contributing

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change. Read more about becoming a contributor in [our GitHub repo](https://github.com/pmarsceill/just-the-docs#contributing).

#### Thank you to the contributors of Just the Docs!

<ul class="list-style-none">
{% for contributor in site.github.contributors %}
  <li class="d-inline-block mr-1">
     <a href="{{ contributor.html_url }}"><img src="{{ contributor.avatar_url }}" width="32" height="32" alt="{{ contributor.login }}"/></a>
  </li>
{% endfor %}
</ul>

### Code of Conduct

Incident Management System is committed to fostering a welcoming community for betterment and growth.

[View our Code of Conduct](https://github.com/ECLK/IncidentManagement/blob/master/CODE_OF_CONDUCT.md) on our GitHub repository.