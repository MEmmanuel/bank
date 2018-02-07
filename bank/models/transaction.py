from django.db.models import Model, fields
from django.db.models.fields.related import ForeignKey, CASCADE

from .account import Account


class Transaction(Model):
    account = ForeignKey(Account, on_delete=CASCADE)
    date = fields.DateTimeField('date')
    label = fields.CharField(max_length=1000)
    value = fields.FloatField()

    class Meta:
        unique_together = (('account', 'date', 'label', 'value'), )

    def __str__(self):
        return 'Transaction: {date} {value} {label}'.format(date=self.date, label=self.label, value=self.value)
