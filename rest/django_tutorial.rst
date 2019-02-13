
Following tutorial from:
https://wsvincent.com/official-django-rest-framework-tutorial-beginners-guide/

instead of pipenv, using virtualenv.
pipenv wasn't readily findable in bofh.
the cluster also using virtualenv.
original tutorial also just use virtualenv.




Once-time Per-Host setup
------------------------

virtualenv venv4django
source     venv4django/bin/activate

pip install django
pip install djangorestframework
pip install pygments


one-time code setup, check into git
-----------------------------------

django-admin startproject tutorial .    # note tailing dot
## cd tutorial


python manage.py startapp snippets


