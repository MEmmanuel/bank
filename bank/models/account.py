import datetime as dt

from django.db.models import Model, fields, aggregates


ACCOUNT_TYPE_LIST = (('CCP', 'CCP'), ('LIVRET A', 'LIVRET A'), ('LDDS', 'LDDS'), ('CEL', 'CEL'), ('PEL', 'PEL'), )


class Account(Model):
    identifier = fields.CharField(max_length=1000)
    type = fields.CharField(choices=ACCOUNT_TYPE_LIST, max_length=len(max(ACCOUNT_TYPE_LIST, key=len)))
    balance_offset = fields.IntegerField(default=0)

    @property
    def current_balance(self):
        from .transaction import Transaction
        return round(self.balance_offset
                     + Transaction.objects
                     .filter(account=self)
                     .aggregate(total_value=aggregates.Sum('value'))['total_value'], 2)

    def get_balance(self, start_date):
        from .transaction import Transaction
        if start_date.month+1 > 12:
            end_date = dt.date(year=start_date.year+1, month=1, day=5)
        else:
            end_date = dt.date(year=start_date.year, month=start_date.month + 1, day=5)
        total = Transaction.objects\
            .filter(account=self, date__gte=start_date, date__lt=end_date)\
            .aggregate(total_value=aggregates.Sum('value'))['total_value']
        if total is None:
            total = 0
        return round(total, 2)

    class Meta:
        unique_together = (('identifier', 'type'), )

    def __str__(self):
        return '{type} account: {identifier}'.format(type=self.type, identifier=self.identifier)
