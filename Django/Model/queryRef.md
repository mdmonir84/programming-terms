# QuerySet Reference

## Query Operation 
- retrieve collection 
  - author_collection = Author.objects.all()
- make list
  - author_list = list(Author.objects.values())
- Specific Query  
  - n1 = Author.objects.get(pk=1)
- filter  
  - author_with_test = Author.objects.filter(name__startswith="test")

## group-by based on ForeignKey 
- keyfunc = lambda author: author['person_id']
- {k:list(g) for k,g in groupby(Author_list, key=keyfunc)}

> import ref: from itertools import groupby

## Create new database entry
- new_author = Author(first_name="Bruce", last_name="Springsteen")
- new_author.save()

- method01
  - p = Author.objects.create(first_name="Bruce", last_name="Springsteen")
- method02 
  - p = Author(first_name="Bruce", last_name="Springsteen")
  - p.save(force_insert=True)

## Extract data from Form POST
- request.POST.get("first_name")


## Mass data load
```
#Sample Database Model 
class Author(models.Model):

    username = models.CharField(max_length=64)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return self.username


#Sample data (JSON format)

[
  {
    "username": "mackchristopher",
    "email": "dcortez@yahoo.com",
    "bio": "Vitae mollitia in modi suscipit similique. Tempore sunt aliquid porro. Molestias tempora quos corporis quam."
  }
]


#Create custom Django command 
#file location: webapp/management/commands/mass_upload.py
#Use can run this command: python manage.py mass_upload
class Command(BaseCommand):

    help = 'Load authors from `data/old_authors.json`'

    DATA_FILE_PATH = os.path.join(settings.BASE_DIR, '..', 'data', 'old_data.json')

    def handle(self, *args, **kwargs):
        with open(self.DATA_FILE_PATH, 'r') as json_file:
            data = json.loads(json_file.read())
        for author in data:
            self._import_author(author)

    def _import_author(self, author_data):
        author = Author(
            username=author_data['username'],
            email=author_data['email'],
            bio=author_data['bio'])
        author.save()


#Run command inside another script
from django.core.management import call_command
call_command('mass_upload')

```
Ref : https://dizballanze.com/en/django-project-optimization-part-2/

## Database query optimization

```
# Sample Model
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

### Accessing Foreign Key Values
- post.author_id
### Bulk Insert on Many to Many Fields
- user.groups.add(administrators, managers)
### Counting QuerySets
```
users = User.objects.all()
users.count()
#Or in template...
{{ users.count }}
```
### Empty QuerySets
```
groups = Group.objects.all()
if groups.exists():
    # Do something...
```
### Reduce Query Counts
```
review = Review.objects.select_related('author').first()  # Select the Review and the Author in a single query
name = review.author.first_name
```
### Select Only What You Need
```
# views.py
# If you don't need the model instance, go for:
invoices = Invoice.objects.values('number', 'date', 'value')  # Returns a dict

# If you still need to access some instance methods, go for:
invoices = Invoice.objects.only('number', 'date', 'value')  # Returns a queryset

# invoices.html
<table>
  {% for invoice in invoices %}
    <tr>
      <td>{{ invoice.number }}</td>
      <td>{{ invoice.date }}</td>
      <td>{{ invoice.value }}</td>
    </tr>
  {% endfor %}
</table>
```
### Bulk Updates
```
from django.db.models import F

Product.objects.update(price=F('price') * 1.2)
```


Ref : https://simpleisbetterthancomplex.com/tips/2016/10/05/django-tip-16-simple-database-access-optimizations.html

