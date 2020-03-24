# Macros

A Macro in Jinja is similar to a function in Python. The idea is to create reusable code by giving it a name. For example:

```
{% macro render_posts(post_list, sep=False) %}
    <div>
        {% for post in post_list %}
            <h2>{{ post.title }}</h2>
            <article>
                {{ post.html|safe }}
            </article>
        {% endfor %}
        {% if sep %}<hr>{% endif %}
    </div>
{% endmacro %}
```

Here we have created a macro named render_posts which takes a required argument named post_list and an optional argument named sep. 

To use a macro call it as follows:

> {{ render_posts(posts) }}

## Key points about macro 
- The macro definition must appear before its use otherwise you will get an error.

- Rather than sprinkling macros in our templates, it is a good idea to store them in a separate file and then import the file as required.

Let’s say we have stored all our macros in a file named macros.html inside the templates directory. Now to import macros from macros.html we use import statement as follows:

> {% import "macros.html" as macros %}

We can now refer to macros defined inside macros.html using the macros variable. For example:

> {{ macros.render_posts(posts) }}

Alternatively, we can also import selected names inside the template using the form statement as follows:

> {% from "macros.html" import render_posts %}

When using macros, you will you encounter cases where you would need to pass an arbitrary number of arguments to a macro.

Similar to *args and **kwargs in Python, inside the macro you have access to varargs and kwargs.

- varargs: It captures additional position arguments passed to the macro as a tuple.
- kwargs: It captures additional keyword arguments passed to the macro as a dictionary.
- caller If the macro was called from a call tag, the caller is stored in this variable as a callable macro.


Although, you have access to these two variables inside macro you don’t need to explicitly declare them in the macro header. 

Here is an example:

```
{% macro custom_renderer(para) %}
    <p>{{ para }}</p>
    <p>varargs: {{ varargs }}</p>
    <p>kwargs: {{ kwargs }}</p>
{% endmacro %}
```
 
> {{ custom_renderer("some content", "apple", name='spike', age=15) }}

In this case, additional positional argument i.e "apple" is assigned to varargs and additional keyword arguments ( name='spike', age=15 ) is assigned to kwargs.


## Additional Examples 

### Example-1

```
{# myapp/templates/macros.html #}

{% macro nav_link(endpoint, text) %}
{% if request.endpoint.endswith(endpoint) %}
    <li class="active"><a href="{{ url_for(endpoint) }}">{{text}}</a></li>
{% else %}
    <li><a href="{{ url_for(endpoint) }}">{{text}}</a></li>
{% endif %}
{% endmacro %}

```

```
{# myapp/templates/layout.html #}

{% from "macros.html" import nav_link with context %}
<!DOCTYPE html>
<html lang="en">
    <head>
    {% block head %}
        <title>My application</title>
    {% endblock %}
    </head>
    <body>
        <ul class="nav-list">
            {{ nav_link('home', 'Home') }}
            {{ nav_link('about', 'About') }}
            {{ nav_link('contact', 'Get in touch') }}
        </ul>
    {% block body %}
    {% endblock %}
    </body>
</html>
```

### Example-2

```
{% macro print_modal(id, title) %}
  <div class="modal fade" id="{{ id }}" tabindex="-1">
    <div class="modal-dialog">
       <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal"><span>&times;</span></button>
          <h4 class="modal-title">{{ title }}</h4>
        </div>
        <div class="modal-body">
          {{ caller() }} <---- {# Look at me! #}
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
  </div>
{% endmacro %}
```
and when you utilize the macro

```
{% call print_modal(someId, someTitle) %}
    {# whatever you put in here will be placed into the {{caller()}} line #}
    {# for example #}
    <h1>HELLO WORLD</h1> {# Will format an h1 into the caller block #}
{% endcall %}
```