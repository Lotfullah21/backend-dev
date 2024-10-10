## save Method:

```py
from django.db import models
from django.utils.text import slugify
class Product(models.Model):
    product_name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.product_name}")
        super(Product, self).save(*args, **kwargs)
```

This method overrides Django’s default save() method to modify or add behavior before saving a Product instance to the database
custom save() method adds extra functionality (slug generation) before handing control to Django's default save() method.

`self.slug = slugify(f"{self.product_name}")`: This generates a slug from the product's name.

The `slugify` function converts a string into a URL-friendly format by:

- Lowercasing the string.
- Replacing spaces with hyphens (-).
- Removing characters that aren’t alphanumeric or hyphens.

`super(Product, self).save(\*args, \*\*kwargs)`: This calls the parent class’s save() method to actually save the object to the database. By calling super(), we re making sure the standard Django save() logic still runs (e.g., saving the instance to the database).

Before saving the product to the database, the method automatically converts the product_name into a URL-friendly slug and assigns it to the slug field.
Then, the object is saved with this slug in the database.

`*args`:

Stands for "arguments" and is used to pass a variable number of non-keyword arguments to a function or method.
In we save method, it's used to allow flexibility so that the method can accept any number of positional arguments.
If there were any extra positional arguments passed to the save() method when it's called, *args would capture them, allowing us to forward them to the parent class's save() method. However, in this particular case, we aren't explicitly using *args.

`**kwargs`
Stands for "keyword arguments" and is used to capture a variable number of keyword arguments (arguments passed by name) in the form of a dictionary.
In we save method, it ensures that any extra keyword arguments passed when calling the save() method are captured and forwarded to the parent class's save() method

```py
product.save(force_insert=True, update_fields=['slug'])
```

### Flow of Execution:

Step 1: When we call product.save(), the custom save() method of we Product class is invoked.
Step 2: Inside we custom method, the slug is generated.
Step 3: The custom method then calls super(Product, self).save(\*args, \*\*kwargs), which invokes Django's default save() method.
Step 4: Django’s save() method takes care of the actual database operations (insertion or updating of the record).

## The two calls are sequential:

we custom save() does some work (slug generation).
It then calls super(), which invokes the parent save() method, which completes the actual saving to the database
