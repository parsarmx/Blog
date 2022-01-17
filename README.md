


Django_Project
======

This project is for a startup

Technologies. 
-------
This is what Techs that we used in our project
s ::
    -> Django
    -> Django Rest Framework
    -> Vue.js
    -> Postgressql
    
Install
-------

**Be sure to use the same version of the code as the version of the docs
you're reading.** You probably want the latest tagged version, but the
default Git version is the main branch. ::

    # clone the repository
    $ git clone https://github.com/parsarmx/Blog.git
    $ cd Blog
    # checkout the correct version

Create a virtualenv and activate it::

    $ python3 -m venv venv
    $ . venv/bin/activate

Or on Windows cmd::

    $ py -3 -m venv venv
    $ venv\Scripts\activate.bat

Install needed apps:

    $ pip install -r requirements.txt .




Run
---

::

    $ python3 manage.py migrate
    $ python3 manage.py runserver

Or on Windows cmd::

    > python manage.py migrate
    > python manage.py runserver

Open http://127.0.0.1:8000 in a browser.



