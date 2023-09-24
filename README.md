# Stage 2 

after going with the installation we are now ready to create our own models and follow the makemigration , migrate phase 
## What is Database Migrations (Django Migrations) ?

database migrations in the context of Django involve managing changes to a database schema while preserving data integrity. These migrations are used to apply changes to the database, such as creating, altering, or deleting tables and columns.

### 1. makemigrations Command 

the makemigrations command is the command that will check if there is any new models is added in your project 
or not  if there is any new update's , it will take responsibility of translating Python Class's to tables inside the Database only translation not excution so a new file with the migration seq will be created with the translated sql form   

```bash
python manage.py makemigrations 
```


### 2. migrate Command 
the migrate command will take the prepared translated file to the excution or stagging phase , in this phase 
class will be translated to be tables inside database so you can perform ORM quiries on it 

```
python manage.py migrate
```
go Check your pgadmin to visualize your tables 

# Usage
those 2 commands  will be applied  each time you will update on models.py  .

# Contributing
If you'd like to contribute to this project, please follow these guidelines for code contributions, bug reporting, and feature requests.

# License
This project is licensed under the MIT License. 
# Acknowledgments
Give credit to any individuals, projects, or libraries that inspired or helped you with this project.


In this revised version, I've broken down the installation steps and provided  clear
