# Django model  

## Important Model Terms 

| FIELD OPTIONS	| DESCRIPTION | 
| ------------- | ------------- |
| Null	        | If True, Django will store empty values as NULL in the database. Default is False.|
| Blank	        | If True, the field is allowed to be blank. Default is False.|
| db_column	    | The name of the database column to use for this field. If this isn’t given, Django will use the field’s name.|
|Default	    | The default value for the field. This can be a value or a callable object. If callable it will be called every time a new object is created.|
|help_text	    | Extra “help” text to be displayed with the form widget. It’s useful for documentation even if your field isn’t used on a form.|
|primary_key	|If True, this field is the primary key for the model.|
|editable	    |If False, the field will not be displayed in the admin or any other ModelForm. They are also skipped during model validation. Default is True.|
|error_messages	|The error_messages argument lets you override the default messages that the field will raise. Pass in a dictionary with keys matching the error messages you want to override.|
|verbose_name	|A human-readable name for the field. If the verbose name isn’t given, Django will automatically create it using the field’s attribute name, converting underscores to spaces.|
|validators	    |A list of validators to run for this field. See the validators documentation for more information.|
|Unique	    |If True, this field must be unique throughout the table.|


Ref : https://www.geeksforgeeks.org/genericipaddressfield-django-models/ 

## Important Foreign Keys
| FIELD OPTIONS	| DESCRIPTION | 
| ------------- | ------------- |
|related_name   | The name to use for the relation from the related object back to this one |
|related_query_name | The name to use for the reverse filter name from the target model |
|to_field   | The field on the related object that the relation is to|

Ref : https://kite.com/python/docs/django.db.models.ForeignKey

## Django Special Model fields
- GenericIPAddressField
- EmailField
- FileField
- ImageField
- URLField
- UUIDField


```
class Node(Model): 
    ip_address = models.GenericIPAddressField(verbose_name="remote address") 
```

## Django two database integration

Ref : 
- https://docs.djangoproject.com/en/3.0/topics/db/multi-db/
- https://books.agiliq.com/projects/django-orm-cookbook/en/latest/multiple_databases.html


## What happens when you save?

When you save an object, Django performs the following steps:

- Emit a pre-save signal. The signal django.db.models.signals.pre_save is sent, allowing any functions listening for that signal to take some customized action.

- Pre-process the data. Each field on the object is asked to perform any automated data modification that the field may need to perform.

Most fields do no pre-processing — the field data is kept as-is. Pre-processing is only used on fields that have special behavior. For example, if your model has a DateField with auto_now=True, the pre-save phase will alter the data in the object to ensure that the date field contains the current date stamp. (Our documentation doesn’t yet include a list of all the fields with this “special behavior.”)

- Prepare the data for the database. Each field is asked to provide its current value in a data type that can be written to the database.

Most fields require no data preparation. Simple data types, such as integers and strings, are ‘ready to write’ as a Python object. However, more complex data types often require some modification.

For example, DateField fields use a Python datetime object to store data. Databases don’t store datetime objects, so the field value must be converted into an ISO-compliant date string for insertion into the database.

- Insert the data into the database. The pre-processed, prepared data is then composed into an SQL statement for insertion into the database.

- Emit a post-save signal. The signal django.db.models.signals.post_save is sent, allowing any functions listening for that signal to take some customized action.



## Database migration

- ./manage.py makemigrations
- ./manage.py migrate 

## Database schema rollback 

For example, if your last two migrations are:

- 0010_previous_migration
- 0011_migration_to_revert

Then you would do:

- ./manage.py migrate my_app 0010_previous_migration 

You can then delete migration 0011_migration_to_revert.

If you're using Django 1.8+, you can show the names of all the migrations with

- ./manage.py showmigrations my_app

To reverse all migrations for an app, you can run:

- ./manage.py migrate my_app zero


## Overriding QuerySet.delete() in Django
We can override a Manager's default QuerySet by overriding the Manager.get_query_set() method.

```
class ModifiedQuerySet(models.query.QuerySet):

    def delete(self):
        pass  # you can throw an exception


class RestrictedDeleteManager(models.Manager):
    def get_query_set(self):
        return ModifiedQuerySet(self.model, using=self._db)

class MyModel(models.Model)
    field1 = ..
    field2 = ..

    objects = RestrictedDeleteManager()
```
