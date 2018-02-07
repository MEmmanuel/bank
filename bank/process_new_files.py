import os
import csv
import datetime as dt

from django.conf import settings
from django.db.models import ObjectDoesNotExist

from bank.tools import *
from bank.models import Account, Transaction


def process_new_files():
    for path in os.listdir(settings.INPUT_FILES_DIR):
        print(okblue('BEGIN integration of: {f}'.format(f=path)))
        account = None
        with open(os.path.join(settings.INPUT_FILES_DIR, path), 'r', encoding='ISO-8859-1') as f:
            for i, row in enumerate(csv.reader(f, delimiter=';')):
                if i == 0:
                    identifier = row[1]
                elif i == 1:
                    try:
                        account = Account.objects.get(identifier=identifier, type=row[1])
                    except ObjectDoesNotExist:
                        raise ValueError('Unknown account: {account_label} {account_type}. Availables: {accounts_list}'
                                         .format(account_label=identifier, account_type=row[1],
                                                 accounts_list=', '.join(map(str, Account.objects.all()))))
                elif i >= 8 and account is not None:
                    date, label, value, francs_value = row
                    date = dt.datetime.strptime(date, '%d/%m/%Y')
                    value = float(value.replace(',', '.'))
                    try:
                        Transaction.objects.get(account=account, date=date, label=label, value=value)
                    except ObjectDoesNotExist:
                        transaction = Transaction.objects.create(account=account, date=date, label=label, value=value)
                        print('Add to {account} ; {transaction}'
                              .format(account=transaction.account, transaction=transaction))

        print(okgreen('END integration of: {f}'.format(f=path)))
        os.remove(os.path.join(settings.INPUT_FILES_DIR, path))
