from django.db.models import Model, fields, aggregates


class Category(Model):
    name = fields.CharField(max_length=1000)

    @property
    def total(self):
        from .transaction import Transaction
        total = Transaction.objects.filter(category=self).aggregate(total_value=aggregates.Sum('value'))['total_value']
        if total is None:
            return 0
        return round(total, 2)

    def __str__(self):
        return 'Category: {name}'.format(name=self.name)
