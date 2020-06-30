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
|help_text	    |Extra “help” text to be displayed with the form widget. It’s useful for documentation even if your field isn’t used on a form.|
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
    ip_address = models.GenericIPAddressField(verbose_name=_("remote address")) 
```

## Django two database integration

Ref : 
- https://docs.djangoproject.com/en/3.0/topics/db/multi-db/
- https://books.agiliq.com/projects/django-orm-cookbook/en/latest/multiple_databases.html
