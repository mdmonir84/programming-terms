
# Adding jQuery Event Listeners to Dynamically Created Django Admin Inline Model Fields

That title has enough keywords to open a safe, yet it is exactly what we're going to be talking about here.

The Django Admin is an incredibly powerful asset that the framework brings to the table; it takes care of dealing with all the CRUD (Create, Read, Update, Delete) operations inherit in every database for you. As an additional plus, it does this in fashion that is incredibly easy to activate and use with any Django project. More often than not, the base functionality of the admin will take care of your use case scenarios. However, there comes times when it's just not sufficient; luckily the admin is easily modified and customized to fit your needs.

In this particular case, I needed to attach jQuery listeners to dynamically created inline model form-sets. When doing so, I got to experience the customizability of the Django admin (as well as an interesting gotcha)

## What Does 'Dynamically Created' Mean?

When working with jQuery we have the ability to bind listeners to specific events. A example usage is when a specific object has been clicked by the user we need to add some HTML to the page to display some additional information. This can be easily done by utilizing jQuery event listeners like this:
```
<html>
    <body>
        <button>Click Me</button>
        <div id="expand"></div>

        <script type="text/javascript" src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
        <script type="text/javascript">
        $(document).ready(function() {
                $("body").click('button', function(e) {
                    console.log('clicked');
                    $("#expand").append("<button>Click me next</button>");
                });
        });
        </script>
    </body>
</html>
```
Click the button and you will see a second button appear next to it. However, if you click on that new button, nothing will happen. This is because there are no listeners bound to that new button that can be triggered, even though our jQuery selector indicates that it is picking up every button element on the page.

There's a significant amount of information about why this is on the jQuery documentation about the on() method, but for our purposes here, lets just make a quick change to our JavaScript to so that buttons that are added to the DOM after page load receive the event listener as well:
```
$(document).ready(function() {
    $("body").on('click', 'button', function(e) {
        $("#expand").append("<button>Click me Next</button>");
    });
});
```
Now, if you reload the page you'll see that any button you click adds another button to the end of the list!

## What is an Inline Field?
An Inline Field is something that the Django admin interface provides through the ability to edit models on the same page as a parent model. This can be quite useful in a multitude of situations, such as in the example given in the documentation where they wish to add multiple Books at the same to a particular Author without having to leave the page. There are two different types of Inline Model Fields that Django provides: StackedInline and TabularInline. The only differences between the two are the templates used to render them.

## Creating and Registering Models
Just so we're all on the same page here, I'm going to setup some example models and bring them into the admin interface. For this example we're going to be working with two models - a Page and its Components. A Page can have many Components, but each Component can only have one Page. Inside our models.py file for the application there should be something that looks like this:
```
from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=255)

class Component(models.Model):
    page = models.ForeignKey(Page, related_name='components')
    text = models.TextField()
    image = models.ImageField(upload_to='component')
```
Once that exists, create an admin.py file in the application directory (this file is not automatically created by the Django startapp command). We will be modifying this file later, but the code below will create the base configuration to work from:
```
from django.contrib import admin

from .models import Page, Component

class ComponentInline(admin.StackedInline):
    model = Component

class PageAdmin(admin.ModelAdmin):
    inlines = [ComponentInline,]

admin.site.register(Page, PageAdmin)
```
## What Did I Just Do?
If you're unfamiliar with the way models are created, I'd recommend reading the excellent Django documentation on Models. Basically what's happened though is that we've created two tables, one to store Pages, and one to store Components. Additionally, because of the Foreign Key we've created a direct relationship between the two different tables - which is how we're able to assign Components a Page to belong to.

Possibly more unfamiliar to you, the admin.py file is already a bit different than the most basic configuration. You'll notice that we've gone beyond the straight forward simple registering of each of the models that we want to appear in the admin.

Remember, the goal here is to have our Component be an Inline. We've done that by creating a ModelAdmin class and passing a StackedInline class of Component into it. If you log into the Django admin now and go to add a new Page, you'll notice that you have the ability to add Components on the same page now through the Inline interface.

Note
Something worth noting is the import line for Page and Component. Notice that the application name is not present in that line; that's not an error. When done this way, the import will look in the same directory as the current module for a module by the name of models.

## Bringing Media into the Django Admin
It's actually surprisingly easy to bring custom CSS and JavaScript into the Django admin interface. To do so, we're going to simply modify the PageAdmin class that we wrote earlier to look like this:

```
class PageAdmin(admin.ModelAdmin):
    inlines = [ComponentInline,]

    class Media:
        js = (
            '/static/<app_name>/admin/pageadmin.js',
        )
```
## Working with jQuery in the Django Admin
Django actually includes jQuery in the admin interface - they're already doing a fair amount with it to handle the features provided by default. We could import our own version of jQuery by adding it to the js list in the Media class of PageAdmin and then work with jQuery as normal.

The problem with that comes when we attempt to attach listeners for dynamically created elements after page load. jQuery won't find them! This is due to the fact that a separate namespace of jQuery was responsible for creating the elements in the first place, so the attached event handlers from our jQuery never were attached to the newly created elements. To fix this we've got to use the Django admin's version of jQuery. To do so, create your pageadmin.js file and add the following to it:

```
(function($) {
    $(document).ready(function) {
        console.log($.fn.jquery);
    });
}(django.jQuery));

```
## Creating an event Handler
If you go visit the Page creation page, then you'll see in your log the output of the version of Django that we have here - you'll notice that it's version 1.4.2. This is true event with the most recent version of Django - 1.5.1. Because we're working with an older version of jQuery when we go to add our event handler we can't use the newer on() method; instead we've got to drop back to using live().

Once we know that, creating the event handler is becomes simple enough:

```
(function($) {
    $(document).ready(function) {
        $("textarea").live('click', function(e) {
            console.log("You clicked a textarea field");
        });
    });
}(django.jQuery))
```

## Using live() and on()
In modern versions of jQuery the live() method has been removed and has been replaced with the on() method. They both serve the same function, which is to add listeners to DOM elements that don't yet exist on page load. To see this in action, visit the Page create page, and click the 'Add another Component' link, and then try clicking in the text area field: you should see a log message about what you just did!
