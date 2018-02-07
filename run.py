import os
import django
from django.db.models import ObjectDoesNotExist

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config")
django.setup()


from bank.models import *
from config import MY_ACCOUNTS, MY_CATEGORIES

for identifier, type, balance_offset in MY_ACCOUNTS:
    try:
        Account.objects.get(identifier=identifier, type=type)
    except ObjectDoesNotExist:
        Account.objects.create(identifier=identifier, type=type, balance_offset=balance_offset)

for category in MY_CATEGORIES:
    try:
        Category.objects.get(name=category)
    except ObjectDoesNotExist:
        Category.objects.create(name=category)

from bank.process_new_files import process_new_files
from bank.export_balances import export_balances

process_new_files()
export_balances()
# for t in Transaction.objects.filter(account=Account.objects.get(type='CCP')).order_by('date'):
#     print(t)
print(Category.objects.all())
