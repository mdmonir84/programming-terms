# JavaScript layout

Django template engine has already provided a tag for inherit your HTML structure called 'extend'.

> Tag "extends" is a using for extends a parent template.
>
> {% extends "base.html" %} uses the literal value "base.html" as the name of the parent template to extend.

base.html is the parent template that can extendable.

```
{% load staticfiles %}
<html lang="en">
    <head><title>Hello World</title></head>
    <body>
        <div id="content">
            {% block content %}{% endblock %}
        </div>

        {% block scripts %}
        <script src="{% static 'js/main.js' %}"></script>
        {% endblock %}

    </body>
</html>
```
and you have another HTML called milk.html that you need everything same as the base.html but include milk.js you just do something like this

```
{% load staticfiles %}
{% extends "base.html" %}

{% block scripts %}
    <!-- block.super will get the content of the block from the parent template -->
    {{ block.super }}
    <script src="{% static 'js/milk.js' %}"></script>
{% endblock %}
```
