django-crumbs
=============

django-crumbs is a pluggable Django app for adding breadcrumbs to your project.

Installation
============
1) Download the app through SVN and add it to your Python path:

    ::

        svn co http://django-crumbs.googlecode.com/svn/trunk/crumbs crumbs

2) Add to your INSTALLED_APPS and run syncdb

    ::

        INSTALLED_APPS = (
            ...,
            'crumbs',
        )


How It Works
============
1) In each template, you'll need to use the add_crumb template tag to append items to the trail:

    ::
    
        # basic crumb without a link
        {% add_crumb 'People' %}
        # crumb with link
        {% add_crumb 'People' 'list_people' %}
        # crumb with link and args
        {% add_crumb person.name 'view_person' person.pk %}


*Note:* no bread crumbs will be printed if only one call to add_crumb has been made.

Setup
=====
1) In your base.html template, add something along the lines of the following code:

    ::
    
        <div id="breadcrumbs">
            {% block breadcrumb %}
                {% load breadcrumb_tags %}
                {% add_crumb 'Home' 'home' %}
            {% endblock %}
            {% render_breadcrumbs %}
        </div>

2) Now in each extended child template, simply add a new crumb to the trail in the breadcrumb block:

    ::
    
        {% block breadcrumb %}
            {{ block.super }}
            {% load breadcrumb_tags %}
            {% add_crumb 'People' 'list_people' %}
        {% endblock %}

Example
=======
1) base.html

    ::
    
        <div id="breadcrumbs">
            {% block breadcrumb %}
                {% load breadcrumb_tags %}
                {% add_crumb 'Home' 'home' %}
            {% endblock %}
            {% render_breadcrumbs %}
        </div>

2) person/list.html

    ::
    
        {% extends "base.html" %}
        {% block breadcrumb %}
            {{ block.super }}
            {% load breadcrumb_tags %}
            {% add_crumb 'People' 'list_people' %}
        {% endblock %}

3) person/view.html

    ::
    
        {% extends "person/list.html" %}
        {% block breadcrumb %}
            {{ block.super }}
            {% load breadcrumb_tags %}
            {% add_crumb person.name 'view_person' person.pk %}
        {% endblock %}
        

Development sponsored by `Caktus Consulting Group, LLC
<http://www.caktusgroup.com/services>`_.
