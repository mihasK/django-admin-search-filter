Django admin search filter
==========================

.. image:: https://img.shields.io/pypi/v/django_admin_search_filter.svg
    :target: https://pypi.python.org/pypi/django_admin_search_filter
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/kragniz/cookiecutter-pypackage-minimal.png
   :target: https://travis-ci.org/kragniz/cookiecutter-pypackage-minimal
   :alt: Latest Travis CI build status

Provides special type of django-admin list filter -- search box with free user input allowed.


Some cases when you need such functionality:

* You have a regular search box for general search (multilpe fields taken into account), but you sometimes need to search **by a specific field**.
* You have a regular search box for flexible substring search, while sometimes you need to **search by exact match**. At the same time number of unique values for this field is too big to display them as choices filter (although in this particular case auto-complete could be a better option)

The solution provided by this package is you place special (configurable) search input as a list filter.


Idea is taken from this Medium article: https://hakibenita.medium.com/how-to-add-a-text-filter-to-django-admin-5d1db93772d8


Usage
-----

# admin.py

.. code-block:: python

    from django_admin_search_filter import get_exact_equals_input_filter, get_icontains_input_filter
    
    ...
    
    class SomeModelAdmin(...):
        ...
        list_filter = (
            ...

            get_icontains_input_filter(title_='name', attrs='name', ),  # Substring search, one field
            get_icontains_input_filter(title_='(alt)name', attrs=('name', 'alt_name') ), # Substring search, several fields
    
            get_exact_equals_input_filter(title_='ID of transaction', attrs='transaction_id', ),  # Exact search, one field
            get_exact_equals_input_filter('ID of transaction/sender/reciever',  # Exact search, several field
                                    attrs=('transaction_id', 'sender_id', 'reciever_id' ))
            
        )





Installation
------------
#. ``pip install django-admin-search-filter``
#.  Add ``"django_admin_search_filter"`` to django's ``INSTALLED_APPS`` (to allow template to be loaded)
#.  Ensure ``APP_DIRS`` set to ``True`` in `templates configuration <https://docs.djangoproject.com/en/4.2/topics/templates/#support-for-template-engines>`_

Requirements
^^^^^^^^^^^^
* Python 3
* Django >= 2.2


Licence
-------
MIT

Authors
-------

`django_admin_search_filter` was written by `Mikhail Koipish <mkoypish@gmail.com>`_.
