from django.db.models import Model, fields


class Category(Model):
    name = fields.CharField(max_length=1000)

    def __str__(self):
        return 'Category: {name}'.format(name=self.name)
