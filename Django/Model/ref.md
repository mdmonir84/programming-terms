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
## Foreign Key 

### related_name
- The name to use for the relation from the related object back to this one. 
- It’s also the default value for related_query_name (the name to use for the reverse filter name from the target model). 
- If you’d prefer Django not to create a backwards relation, set related_name to '+' or end it with '+'. 
- For example, this will ensure that the User model won’t have a backwards relation to this model:

```
user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name='+',
)
```
## Acution about related_name and related_query_name
- If you are using related_name or related_query_name on a ForeignKey or ManyToManyField, you must always specify a unique reverse name and query name for the field. 
- This would normally cause a problem in `abstract base classes`, since the fields on this class are included into each of the child classes, with exactly the same values for the attributes (including `related_name` and `related_query_name`) each time.
- To work around this problem, when you are using `related_name` or `related_query_name` in an abstract base class (only), part of the value should contain `'%(app_label)s' and '%(class)s'`.
- `'%(class)s'` is replaced by the lowercased name of the child class that the field is used in.
- `'%(app_label)s'` is replaced by the lowercased name of the app the child class is contained within. 
- Each installed application name must be unique and the model class names within each app must also be unique, therefore the resulting name will end up being different.

```
For example, given an app common/models.py:

from django.db import models

class Base(models.Model):
    m2m = models.ManyToManyField(
        OtherModel,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

    class Meta:
        abstract = True

class ChildA(Base):
    pass

class ChildB(Base):
    pass
```

## Databasee Manager 



## Multiple Database Setup 

## Database Mapping 
![database-mapping](images/database_mapping.png)

## Database Mapping without router
![database-router](images/database_router.png)
## Update Settings

```
DATABASE_ROUTERS = ['project<name>.router.DbRouter']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': '******',
        'PASSWORD': '******',
        'HOST': 'localhost',
        'PORT': '',
    },
	'app_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'file::memory:',
    },
}

```

## Database Router 

```
class DbRouter:
    """
    A router to control all database operations on models in the
    user application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read 'app-1' models go to app_db.
        """
        if model._meta.app_label == 'app-1':
            return 'app_db'
		# Otherwise no opinion, defer to other routers or default database
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write 'app-1' models go to app_db.
        """
        if model._meta.app_label == 'app-1':
            return 'app_db'
        # Otherwise no opinion, defer to other routers or default database
		return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the 'app-1' is involved.
        """
        if obj1._meta.app_label == 'app-1' or \
           obj2._meta.app_label == 'app-1':
           return True
        # Otherwise no opinion, defer to other routers or default database
		return None

	def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the 'app-1' only appears in the 'app_db'
        database.
        """
		if db == 'app_db':
            # Migrate Django 'app-1' models if current database is 'app_db'
            if app_label =='app-1':
                return True            
            else:
                # Non Django 'app-1' models should not be migrated if database is 'app_db'
                return False
        # Otherwise no opinion, defer to other routers or default database
        return None

	# def allow_syncdb(self, db, model):
        # """
        # Make sure the 'app-1' app only appears on the 'other' db
        # """
        # if db == 'app_db':
            # return model._meta.app_label == 'app-1'
        # elif model._meta.app_label == 'app-1':
            # return False
        # return None

```


## Database model needs to update 

```
class Model01(models.Model):
    ..... = models.DecimalField(
						max_digits=19, 
						decimal_places=4,
						
						)
						

    . . .
        class Meta:
            app_label = 'app-1'

```

## Without Database Router 
### Migration command to specific database
  - python manage.py migrate --database=node_db

### Database operation while multiple database
```
# Query
# This will run on the 'default' database.
Mode.objects.all()

# So will this.
Memory.objects.using('node_db').all()

# This will run on the 'other' database.
Cpu.objects.using('node_db').all()

# Save 
my_object.save(using='legacy_users')

# Query & save
p = Person(name='Fred')
p.save(using='first')  # (statement 1)
p.save(using='second') # (statement 2)

# Query & delete
u = User.objects.using('legacy_users').get(username='fred')
u.delete() # will delete from the `legacy_users` database
```