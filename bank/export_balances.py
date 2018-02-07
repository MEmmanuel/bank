import datetime as dt

from django.conf import settings
from django.template.loader import render_to_string

from bank.models import Account, Transaction


def export_balances():
    older_transaction_date = Transaction.objects.all().order_by('date')[0].date
    start_date = dt.date(year=older_transaction_date.year, month=older_transaction_date.month, day=5)
    if dt.date.today().day < 5:
        date = dt.date(year=dt.date.today().year, month=dt.date.today().month-1, day=5)
    else:
        date = dt.date(year=dt.date.today().year, month=dt.date.today().month, day=5)

    accounts_l = Account.objects.all()
    month_balances = [{
        'month': 'Aujourd\'hui',
        'balances': list(map(lambda account: account.current_balance, accounts_l))
    }]
    month_balances[0]['balances'] += ['', round(sum(month_balances[0]['balances']), 2)]
    available_money = round(sum(map(lambda account: account.current_balance, Account.objects.exclude(type='PEL'))), 2) - 300 - 15
    while date >= start_date:
        balances = list(map(lambda account: account.get_balance(date), accounts_l))
        month_balances.append(
            {
                'month': date.strftime('%m-%Y'),
                'balances': balances + [
                    round(sum(balances), 2),
                    round(month_balances[-1]['balances'][-1] - sum(balances), 2)
                ]
            }
        )
        if date.month-1 < 1:
            date = dt.date(year=date.year-1, month=12, day=5)
        else:
            date = dt.date(year=date.year, month=date.month-1, day=5)

    with open(settings.OUTPUT_FILE_PATH, 'w') as f:
        f.write(render_to_string('output.html', {
            'columns': ['Mois'] + list(map(str, accounts_l)) + ['Bilan', 'Total cumulé'],
            'values': month_balances,
            'available_money': available_money
        }))
