# Movie Rating and Review website

Books library website created using Python and Django web framework which will allow users to check book information, allow users to add new books and update existing information about book.

## Requirements

Python

Django

Cripsy forms (For easy forms styling)



```bash
pip install django-crispy-forms
```


## APIs Used

 - API to retrieve book information from database by book name or book publish year

 - API to add new book with all the required information

 - API to update book related data


## More Details

 - App 'movie':

     - Implemented template inheritance functionality provide by Django. 
Code in 'base.html' is inherited in all the required templates.

     - Website will open 'home.html' by default. 
 
     - Used 'crispy' forms for easy implementation of form styling.

- Database :

     - Created superuser(Admin user) with ID 'AdminUser' and password 'admin@123'.
Only this admin user can have access to the Django default admin panel and can add new book with it's description directly from Django admin panel.

     - Added some books with their descriptions to have basic functionality working.
  
     - Please visit Django admin panel to view all the books and the data added.


## Get started

 - Download or clone this Git repository

 - On local system run the project with following command in command prompt
```bash
repo_path>python manage.py runserver
```

