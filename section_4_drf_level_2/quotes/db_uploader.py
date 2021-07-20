

import os
import django
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes.settings")
django.setup()

from quote.models import Quote
csv_path = '/Users/adam/github/drf_and_vuejs/section_4_drf_level_2/quotes/quote_list.csv'

with open(csv_path, mode='r') as q:
    reader = csv.reader(q)

    for i in reader:
        i = ''.join(i).split('.')
        number = int(i[0])
        body = ''.join(i[1:]).replace('–', '$').replace(
            '-', '$').strip('$').split('$')
        text = body[0].strip()
        source = body[-1].strip() if len(body) > 1 else 'Null'
        Quote.objects.create(
            quote_author=source,
            quote_body=text
        )
