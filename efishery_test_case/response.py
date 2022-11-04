from tabulate import tabulate
from currency_converter import CurrencyConverter
import datetime
import json
import pandas as pd


def get_response(res, context=None, c_value=None):
    if res.ok:
        dataset = json.loads(res.text)
        if dataset:
            if context == 'get_max_price':
                df = pd.DataFrame(dataset, columns=dataset[0].keys())
                df['tgl_parsed'] = pd.to_datetime(df['tgl_parsed']) - pd.to_timedelta(7, unit='d')
                df = df.groupby(['komoditas', pd.Grouper(key='tgl_parsed', freq='W-MON')]).agg(price = ('price' , 'max')).round()
                print (df)
                return False
            elif context == 'get_most_records':
                df = pd.DataFrame(dataset, columns=dataset[0].keys())
                result = df['komoditas'].value_counts()
                print (result)
                return False
            elif context == 'get_aggregation_price':
                dataset[:] = [d for d in dataset if str(d.get('price')).isdigit()]
                df = pd.DataFrame(dataset, columns=dataset[0].keys())
                result = df.groupby(c_value).agg({"price": ['min', 'max']})
                print(result)
                return False
            elif context == 'get_by_range_price':
                dataset[:] = [d for d in dataset if str(d.get('price')).isdigit() and c_value[0] <= int(d.get('price')) <= c_value[1]]
            elif context == 'get_all_by_range':
                df = pd.DataFrame(dataset, columns=dataset[0].keys())

                date_one = datetime.datetime.strptime(c_value[2][0], '%Y-%m-%d').date()
                date_two = datetime.datetime.strptime(c_value[2][1], '%Y-%m-%d').date()

                df['tgl_parsed'] = pd.to_datetime(df['tgl_parsed']).dt.date

                result = df.loc[
                        (df['price'].isin(c_value[0])) &
                        (df['size'].isin(c_value[1])) &
                        ((df['tgl_parsed'] > date_one) & (df['tgl_parsed'] < date_two) )
                ]
                if not result.empty:
                    print(result)
                else:
                    print('data not found')
                return False

            c = CurrencyConverter()
            rows = []
            for idx, x in enumerate(dataset):
                if idx > 9:
                    break
                x['no'] = idx + 1
                if context != 'get_most_records':
                    x['price_in_usd'] = (c.convert(x.get('price'), 'IDR', 'USD'))
                rows.append(x.values())
            header = dataset[0].keys()
            print(tabulate(rows, header))
        else:
            print('data not found')
    else:
        print('server error')


def get_option_response(res):
    if res.ok:
        dataset = json.loads(res.text)
        if dataset:
            rows = []
            for x in dataset:
                rows.append(x.values())
            header = dataset[0].keys()
            print(tabulate(rows, header))
        else:
            print('data not found')
    else:
        print('server error')


def simple_response(res, session, text='data successfully'):
    if res.ok:
        session.cache.clear()
        print(text)
    else:
        print('server error')
