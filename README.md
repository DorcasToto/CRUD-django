#  Crud-django

#### Author: [DorcasCherono](https://github.com/DorcasToto)


## Admin Requirements

As a admin of the web application you will be able to:

1. Sign up and log in
2. List veterinary officers
3. Onboard a veterinary officer
4. Update a veterinary officer's information
5. Deactivate a veterinary officer


## Endpoints
Download [ postman]( https://www.postman.com/downloads/ ) to access the following endpoints

* [ Login endpoint ]( http://127.0.0.1:8000/api/login/ )
* [ Register admin endpoint ]( https://fugaadmin.herokuapp.com/api/add_admin/ )
* [ List Vets endpoint ]( https://fugaadmin.herokuapp.com/api/vets/ )
* [ Onboard a vet endpoint ]( https://fugaadmin.herokuapp.com/api/vets/ )
* [ Deactivate a vet endpoint ]( https://fugaadmin.herokuapp.com/api/vets/<id>/ )
* [ Update a vet endpoint ]( https://fugaadmin.herokuapp.com/api/vets/<id>/ )

    #### NB
    * Replace `<id>` in the endpoints with the id you would like to modify
        
                           


## Setup and installations
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements.txt file.
* On your terminal run `python3.6 manage.py runserver`
* Access the live site using the local host provided



## Getting started

### Prerequisites
* python3.6
* virtual environment
* pip3

#### Clone the Repo and rename it to suit your needs.
```bash
git clone https://github.com/DorcasToto/CRUD-django
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.6 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY = 'your secret key'
DEBUG=True
DB_NAME='<your database name>'
DB_USER='<your database user>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='*'
DISABLE_COLLECTSTATIC=1
```

#### Install dependencies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.6 manage.py check
python manage.py makemigrations veterinary
python3.6 manage.py sqlmigrate veterinary 0001
python3.6 manage.py migrate
```

#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)

        
## Built With

* [Python3.6](https://docs.python.org/3/)
* Django 3.1
* Postgresql 
* Boostrap
* HTML
* CSS

### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license/MIT)