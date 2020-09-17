# ION - Racing web app

## INFO
      DONT TOUCH master_ionracing.yml!

## Application structure
      /ION-Racing-Azure
            ├── app/
            │   ├── __init__.py
            │   ├── routes.py
            │   ├── forms.py
            │   ├── schema.sql
            │   |
            │   ├── templates/
            │   │   |── index.html
            │   |
            │   |── static/
            │   │   ├── css/
            │   │   │   ├── style.css
            │   │   ├── js/
            │   │   │   ├── app.js
            │         
            ├── venv/
            ├── config.py
            ├── requirements.txt
            ├── database.db
            ├── .gitignore
            ├── README.md
            └── ionracing.py

## Getting Started
            1. Setting-up virtualenv (command, python 3.3*)
                  -> python -m venv venv

            2. Activate virtualenv (command)
                  -> OS X / Linux: source venv/bin/activate
                  -> Windows: venv\Scripts\activate
            3. Pip install dependencies 
                  -> Need to install all dependencies before starting to work on the project

            Uninstalling dependencies if needed: pip uninstall [options] <package> ...