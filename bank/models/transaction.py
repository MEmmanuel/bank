from django.db.models import Model, fields
from django.db.models.fields.related import ForeignKey, CASCADE

from .account import Account
from .category import Category


class Transaction(Model):
    account = ForeignKey(Account, on_delete=CASCADE)
    date = fields.DateTimeField('date')
    label = fields.CharField(max_length=1000)
    value = fields.FloatField()
    category = ForeignKey(Category, null=True)

    def categorize(self, category_matching):
        for m, c in category_matching:
            if m in self.label:
                self.category = c
                self.save()
                break

    class Meta:
        unique_together = (('account', 'date', 'label', 'value'), )

    def __str__(self):
        return 'Transaction: {date} {value} {label}'.format(date=self.date, label=self.label, value=self.value)
