from tabulate import tabulate
from collections import Counter
from currency_converter import CurrencyConverter
import json
import pandas as pd


def get_response(res, context=None, c_value=None):
    if res.ok:
        dataset = json.loads(res.text)
        if dataset:
            if context == 'get_max_price':
                dataset = sorted(dataset, key=lambda d: d['price'], reverse=True)
            elif context == 'get_most_records':
                receivers = [d[c_value] for d in dataset]
                counter = [dict(Counter(receivers))]
                dataset = sorted(counter, key=lambda d: d, reverse=True)
            elif context == 'get_aggregation_price':
                dataset[:] = [d for d in dataset if str(d.get('price')).isdigit()]
                df = pd.DataFrame(dataset, columns=dataset[0].keys())
                result = df.groupby(c_value).agg({"price": ['min', 'max']})
                print(result)
                return False
            elif context == 'get_by_range_price':
                dataset[:] = [d for d in dataset if str(d.get('price')).isdigit() and c_value[0] <= int(d.get('price')) <= c_value[1]]

            c = CurrencyConverter()
            rows = []
            for x in dataset:
                if context != 'get_most_records':
                    x['price_in_usd'] = (c.convert(x.get('price'), 'IDR', 'USD'))
                rows.append(x.values())
            header = dataset[0].keys()
            print(tabulate(rows, header))
        else:
            print('data not found')
    else:
        print('server error')


def simple_response(res, text='data successfully'):
    if res.ok:
        print(text)
    else:
        print('server error')
