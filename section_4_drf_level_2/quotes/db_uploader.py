import os
import django
import csv

#from quote.models import Quote

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes.settings")
django.setup()

with open('/Users/adam/github/drf_and_vuejs/section_4_drf_level_2/quotes/quote_list.csv', mode='r') as q:
    reader = csv.reader(q)

    for i in reader:
        print(i)
