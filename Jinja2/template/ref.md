# Template 
## Includes 

The include statement renders a template inside another template. The include statement is commonly used to render a static section which is repeated throughout the site. Here is the syntax of the include statement:

> {% include 'path/to/template' %}

Let’s say we have a simple navigation bar stored in nav.html inside templates directory as follows:

```
<nav>
    <a href="/home">Home</a>
    <a href="/blog">Blog</a>
    <a href="/contact">Contact</a>  
</nav>
```

To include the navigation bar inside home.html, we use the following code:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
 
    {# including the navigation bar from nav.html #}
    {% include 'nav.html' %}   
 
</body>
</html>
```
Output:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
 
<nav>
    <a href="/home">Home</a>
    <a href="/blog">Blog</a>
    <a href="/contact">Contact</a>
</nav>
 
</body>
</html>
```

## Template Inheritance

Template Inheritance is one the most powerful aspects of Jinja Templating. The idea behind template inheritance is somewhat similar to Object Oriented Programming. We start by creating a base template which contains the HTML skeleton and markers that child template can override. The markers are created using the block statement. The child templates uses extends statement to inherit or extends the base templates. Let’s take an example:

```
{# This is templates/base.html template #}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Default Title{% endblock %}</title>
</head>
<body>
 
    {% block nav %}
        <ul>
            <li><a href="/home">Home</a></li>
            <li><a href="/api">API</a></li>
        </ul>
    {% endblock %}
 
    {% block content %}
 
    {% endblock %}
 
</body>
</html>
```

This is our base template base.html. It defines three blocks using the block statement where child templates can fill in. The block statement takes a single argument which is the name of the block. Inside the template, the block name must be unique otherwise you will get an error.

A child template is a template which extends the base template. The child template may add, override or leave along the contents of the parent block. Here is how we can create a child template.

```
{# this is templates/child.html template #}
{% extends 'base.html' %}
  
{% block content %}
    {% for bookmark in bookmarks %}
        <p>{{ bookmark.title }}</p>
    {% endfor %}
{% endblock %}
```

The extends statement tells Jinja that child.html is a child template and inherits from base.html. When Jinja encounters the extends statement it loads the base template i.e base.html then replaces the blocks of content in the parent template with the blocks of content of the same name in the child template. In case, a block of matching name isn’t found in the child template then the block from parent template will be used.

Note that in the child template we are only overriding the content block, so the default content from the title and nav will be used while rendering child template. The output should look like this:

```
<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title>Default Title</title>
</head>
<body>
    
    <ul>
        <li><a href="/home">Home</a></li>
        <li><a href="/api">API</a></li>
    </ul>
 
    <p>Bookmark title 1</p>
    <p>Bookmark title 2</p>
    <p>Bookmark title 3</p>
    <p>Bookmark title 4</p>
 
 
</body>
</html>
```
If we want, we can change the default the title by overriding the title block in the child.html as follows:

```
{# this is templates/child.html template #}
{% extends 'base.html' %}
 
{% block title %}
    Child Title 
{% endblock %}
 
{% block content %}
    {% for bookmark in bookmarks %}
        <p>{{ bookmark.title }}</p>
    {% endfor %}
{% endblock %}
```
After overriding a block you can still refer to the content in the parent template by calling super() function. The super() call is generally used when child template needs to add its own content in addition to the content from the parent. For example:

```
{# this is templates/child.html template #}
{% extends 'base.html' %}
 
{% block title %}
    Child Title 
{% endblock %}
 
{% block nav %}
    {{ super() }} {# referring to the content in the parent templates #}
    <li><a href="/contact">Contact</a></li>
    <li><a href="/career">Career</a></li>
{% endblock %}
 
{% block content %}
    {% for bookmark in bookmarks %}
        <p>{{ bookmark.title }}</p>
    {% endfor %}
{% endblock %}
```
Output:

```
<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title>Child Title</title>
</head>
<body>
    
    <ul>
        <li><a href="/home">Home</a></li>
        <li><a href="/api">API</a></li>
        <li><a href="/contact">Contact</a></li>
        <li><a href="/career">Career</a></li>
    </ul>
 
    <p>Bookmark title 1</p>
    <p>Bookmark title 2</p>
    <p>Bookmark title 3</p>
    <p>Bookmark title 4</p>
 
 
</body>
</html>
```
