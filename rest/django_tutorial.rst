
Following tutorial from:
https://wsvincent.com/official-django-rest-framework-tutorial-beginners-guide/

instead of pipenv, using virtualenv.
pipenv wasn't readily findable in bofh.
the cluster also using virtualenv.
original tutorial also just use virtualenv.




Once-time Per-Host setup
------------------------

virtualenv --python=python3 venv4django
source     venv4django/bin/activate

pip install django
pip install djangorestframework
pip install pygments


one-time code setup, check into git
-----------------------------------

django-admin startproject tutorial .    # note tailing dot


## cd tutorial    # wsvincent.com didn't cd ... 

python manage.py startapp snippets   # thus this was created in the same level as the tutorial project 


created snippets/model.py

but 
python manage.py makemigrations snippets 
fails in bofh, even when vent python default to py3

what's going on??
