from django.db import models



class Phone(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def __str__(self):
        return f'{self.id}; {self.name}; {self.price}; {self.image}; {self.release_date};' \
               f'{self.lte_exists}; {self.slug}'
