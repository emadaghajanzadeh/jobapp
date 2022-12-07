from django.db import models
from django.utils.text import slugify

# Create your models here.
class JobPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField()
    # Slug is being used to provide us with user-friendly URLs
    # Unique helps us with indexing
    slug = models.SlugField(null=True, max_length=40, unique=True)
    
    # String representation of objects
    def __str__(self):
        return self.title

    # When the object wants to be saved this function is executed.
    def save(self, *args, **kwargs):
        # We do this because we do not want slugs to be updated whenever we update the objects (They must only get value once object is created)
        # if ID does not exist:
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost, self).save(*args, **kwargs)

# You can manipulate data inside this table by using shell commands:
    # Type python manage.py shell
    # from app.models import JobPost
    # JobPost.objects.create() or JobPost.objects.filter()
    # JobPost.objects.get()
    # JobPost.objects.exclude() => exactly opposite to filter() => it returns all objects that dont have those properties.
    # JobPost.objects.filter()[1:2] => Filter returned objects
    # JobPost.objects.order_by("title") => sort objects based on the arguments you send to the function. ("-title") for descending order
# But if you want to have >< filtering, the above filter function does not help and u should use Field Lookups: https://docs.djangoproject.com/en/4.1/ref/models/lookups/
    # {fieldname}__{lookup}
    # JobPost.objects.filter(salary__gte = 1000)


# Aggregation:
# JobPost.objects.count()
# JobPost.objects.aggregate(Avg("salary"))
# Avg Salary of only two first jobs:
# JobPost.objects.filter(id__lte=2).aggregate(Avg("salary"))
# How much max is greater than mean: (Complex aggregates need alias, name in other words)
# JobPost.objects.aggregate(calculated_diff = Max("salary") - Avg("salary"))
    

    

    

