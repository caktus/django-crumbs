django-crumbs
=============

django-crumbs is a pluggable Django app for adding breadcrumbs to your project.

Installation
============

1) Install django-crumbs with pip::

    pip install django-crumbs

2) Add to your INSTALLED_APPS and run syncdb::

    INSTALLED_APPS = (
        ...,
        'crumbs',
    )

3) Make sure you have the "request" context processor in your config::

    TEMPLATE_CONTEXT_PROCESSORS += ['django.core.context_processors.request']

How it Works
============

django-crumbs provides two template tags. One (``add_crumb``) adds a breadcrumb
to the current breadcrubs, the other (``render_breadcrumbs``) actually renders the
accumulated breadcrumbs.

In your base template, you will generally include a template block that uses
``add_crumb`` to set up an initial first breadcrumb. You can then extend
the breadcrumbs by defining the same block in child templates, using
``{{ block.super }}`` to maintain the content from parent templates, and
adding additional breadcrumbs with additional ``add_crumb`` tags.

To render the accumulated breadcrumbs, include the ``render_breadrubms`` tag
in the base template after the block which accumulates the breadcrumbs.

Example
=======

1) base.html::

        <div id="breadcrumbs">
            {% block breadcrumb %}
                {% load breadcrumb_tags %}
                {% add_crumb 'Home' 'home' %}
            {% endblock %}
            {% render_breadcrumbs %}
        </div>

2) person/list.html::

        {% extends "base.html" %}
        {% block breadcrumb %}
            {{ block.super }}
            {% load breadcrumb_tags %}
            {% add_crumb 'People' 'list_people' %}
        {% endblock %}

3) person/view.html::

        {% extends "person/list.html" %}
        {% block breadcrumb %}
            {{ block.super }}
            {% load breadcrumb_tags %}
            {% add_crumb person.name 'view_person' person.pk %}
        {% endblock %}


Requirements
============

- django >= 1.3

Django 1.3 is the minimum level that is currently tested, it's likely that the django-crumbs code
still works fine on earlier Django versions.


Development sponsored by `Caktus Consulting Group, LLC
<http://www.caktusgroup.com/services>`_.

