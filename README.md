<p align="center">
  <a href="https://github.com/prostiate/pranala_resource"><img src="https://lh6.googleusercontent.com/HNsxNXfQ5doC4JlsSxgn_jYA_PDn5dDKfd_lEb_bFCGTWfs0lfDchdRy0iIfmIcghxHa9JbAVH8N9dnLdDIkOkpZ7EoLEq0-cUKB1X-TfIt4wWOKwup9RfTmLcm7vOEfpQTWNqQG" alt="Pranala"></a>
</p>
<p align="center">
    <em>Pranala Resource is a library with build-in CLI application that users will can interact.</em>
</p>
<p align="center">
<a href="https://github.com/tiangolo/typer/actions?query=workflow%3ATest" target="_blank">
    <img src="https://github.com/tiangolo/typer/workflows/Test/badge.svg" alt="Test">
</a>
</p>

---
# Pranala Resources CLI and Wrapper
Pranala Resource is a library with build-in CLI application that users will can interact. Based on Python 3.8+.

Typer is used to build CLI application. 

List of commands:
```commandline
Commands:
  add-records            Add a record
  delete-records         Update records with condition and value.
  get-aggregation-price  get aggregation price by the specified column
  get-all-by-commodity   get by commodity
  get-all-by-range       get all by range harga, size and tanggal
  get-by-area            get by area province and city
  get-by-id              get by uuid
  get-by-range-price     get by range price
  get-max-price          get max price by week and commodity
  get-most-records       get most records by commodity
  update-records         Update records with condition and value.
```

## Structure Project
```
/efishery_test_case/__init__.py     # 
/efishery_test_case/__main__.py     # main class, including typer app() comand
/efishery_test_case/helpers.py      # validations, formatting strings
/efishery_test_case/response.py     # display the response
/tests/__init__.py                  # 
/tests/pranala_tests.py             # unit test
.gitignore                          # 
Dockerfile                          # docker build
main.py                             # main application, will run typer command app()
pranala_cache.sqlite                # request_cache stored in sqlite
README.md                           # readme
requirements.txt                    # requirements packages
```

## Installation
```commandline
pip install -r /path/to/requirements.txt
```

## Docker Build
```commandline
docker build -t pranala:latest .
docker run pranala:latest
```

## Usages
You can use `--help` arguments to see all the available commands.
```commandline
(py8) PS C:\case> python .\main.py pranala --help
Usage: main.py pranala [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add-records            Add a record
  delete-records         Update records with condition and value.
  get-aggregation-price  get aggregation price by the specified column
  get-all-by-commodity   get by commodity
  get-all-by-range       get all by range harga, size and tanggal
  get-by-area            get by area province and city
  get-by-id              get by uuid
  get-by-range-price     get by range price
  get-max-price          get max price by week and commodity
  get-most-records       get most records by commodity
  update-records         Update records with condition and value.
```

### Add a record
You can add a record using `add-records` and then it will show prompt. You can use `--help` arguments to see requirements input.
```commandline
(py8) PS C:\laragon\www\efishery-test-case> python .\main.py pranala add-records --help
Usage: main.py pranala add-records [OPTIONS]

  Add a record

Options:
  --commodity TEXT  [required]
  --province TEXT   [required]
  --city TEXT       [required]
  --size TEXT       [required]
  --price TEXT      [required]
  --help            Show this message and exit.
```
```commandline
(py8) PS C:\laragon\www\efishery-test-case> python .\main.py pranala add-records
Commodity: gurame
Province: jawa tengah
City: cilacap
Size: 30
Price: 30000
data successfully created
```

### Update a record
You can update a record using `update-records` and you need to use `--condition condition1=value1,condition2=value2 --set-value column1=value1,column2=value2` in order to update the data.
```commandline
(py8) PS C:\laragon\www\efishery-test-case> python .\main.py pranala update-records --help
Usage: main.py pranala update-records [OPTIONS]

  Update records with condition and value. Example: --condition
  uuid=123,komoditas=GURAME --set-value komoditas=GURAME,area_provinsi=JAWA
  BARAT

Options:
  --condition TEXT
  --set-value TEXT
  --help            Show this message and exit.
```
```commandline
(py8) PS C:\laragon\www\efishery-test-case> python .\main.py pranala update-records --condition uuid=13806864-4557-42d4-926c-050e4d54d671 --set-value size=170
condition:  {'uuid': '13806864-4557-42d4-926c-050e4d54d671'}
set_value:  {'size': '170'}
date successfully updated
```

### Delete a record
You can delete a record using `delete-records` and you need to use `--condition condition1=value1,condition2=value2` in order to delete the data. After you enter those command and input the data, it will show a prompt to confirm the operation.
```commandline
(py8) PS C:\case> python .\main.py pranala delete-records --help
Usage: main.py pranala delete-records [OPTIONS]

  Update records with condition and value. Example: --condition
  uuid=123,komoditas=GURAME

Options:
  --condition TEXT
  --action / --no-action  [required]
  --help                  Show this message and exit.
```
```commandline
(py8) PS C:\case> python .\main.py pranala delete-records --condition uuid=1add5c6e-fec2-45c0-8a2f-ff1782bf8b46
Are you sure you want to delete the record? [y/n]: n
Operation cancelled
```
```commandline
(py8) PS C:\case> python .\main.py pranala delete-records --condition uuid=1add5c6e-fec2-45c0-8a2f-ff1782bf8b46
Are you sure you want to delete the record? [y/n]: y
Deleting...
data successfully deleted
```

### Get Aggregation Price Based On Specified Inputted Column
You can get aggregate price using `get-aggregation-price` and it will show a prompt to user to input the column name.
```commandline
(py8) PS C:\case> python .\main.py pranala get-aggregation-price --help
Usage: main.py pranala get-aggregation-price [OPTIONS]

  get aggregation price by the specified column

Options:
  --by TEXT  [required]
  --help     Show this message and exit.
```
```commandline
(py8) PS C:\case> python .\main.py pranala get-aggregation-price
By: komoditas
            price
              min    max
komoditas
BANDENG     13000  98000
BAWAL        1000  97000
GURAME      10000  96000
LELE        12000  93000
MAS          1000  98000
NILA HITAM  10000  90000
NILA MERAH  10000  96000
PATIN        1000  98000
```

### Get All Data Based On Specified Commodity
You can get all data based on specified commodity using `get-all-by-commodity` and it will show a prompt to user to input the value of commodity.
```commandline
(py8) PS C:\laragon\www\efishery-test-case> python .\main.py pranala get-all-by-commodity --help
Usage: main.py pranala get-all-by-commodity [OPTIONS]

  get by commodity

Options:
  --komoditas TEXT  [required]
  --help            Show this message and exit.
```
```commandline
(py8) PS C:\laragon\www\efishery-test-case> python .\main.py pranala get-all-by-commodity
Komoditas: gurame
uuid                                  komoditas    area_provinsi     area_kota      size    price  tgl_parsed                timestamp    no    price_in_usd
------------------------------------  -----------  ----------------  -----------  ------  -------  --------------------  -------------  ----  --------------
2c75f19f-ac7a-4c28-9459-8fbb64c8cb00  GURAME       JAWA TENGAH       PURWOREJOL       40    55000  2022-01-01T13:11:46Z  1641042706799     1        3.58106
b175e2c0-a97e-4cf4-b16f-ab8f59c1a429  GURAME       KALIMANTAN TIMUR  BORNEO           30    87000  2022-01-01T23:34:16Z  1641080056368     2        5.66459
7ffda1e2-163d-4430-a661-5c29b1eac424  GURAME       JAWA TENGAH       PURWOREJO       110     3000  2022-01-02T01:33:44Z  1641087224309     3        0.195331
c4f6ed2f-a4a3-4773-b712-e514f4182be9  GURAME                                         120    90000  2022-01-16T06:22:46Z  1642314166739     4        5.85992
78de9a12-cac7-410d-abb5-d40874bfd881  GURAME       JAWA TENGAH       PURWOREJOR      110    85000  2022-01-29T02:15:49Z  1643422549714     5        5.53436
9210ca57-b15f-431f-9135-67126dd7c6f0  GURAME       JAWA TIMUR        BANYUWANGI      130    73000  2022-02-02T16:25:38Z  1643819138296     6        4.75304
6c8bfe30-ded7-4b6b-bdaf-1b5f3ea33cbd  GURAME       JAWA BARAT        CIMAHI          200    96000  2022-02-10T00:38:55Z  1644453535618     7        6.25058
eb353254-49cb-49a2-900e-43da80cfa2f7  GURAME       JAWA TENGAH       PURWOREJOR      110    57000  2022-02-10T08:44:37Z  1644482677674     8        3.71128
c7b0d94c-553d-49c7-91d1-6ffbb59b872a  GURAME       JAWA TIMUR        PROBOLINGGO      60    38000  2022-02-12T08:48:20Z  1644655700611     9        2.47419
6f57732f-9a26-4e0e-8152-abacba6c5cdd  GURAME       JAWA TENGAH       TEGAL           160    69000  2022-02-18T05:50:20Z  1645163420277    10        4.4926
```

### Get All Data Based On Specified Range Price, Size And Date
You can get all data based on specified range of price, size and date using `get-all-by-range` and it will show a prompt to user to input the range of price, size and date.

All data must be present and must follow the given format
```commandline
(py8) PS C:\laragon\www\efishery-test-case> python .\main.py pranala get-all-by-range --help
Usage: main.py pranala get-all-by-range [OPTIONS]

  get all by range harga, size and tanggal

Options:
  --range-harga TEXT    [required]
  --range-size TEXT     [required]
  --range-tanggal TEXT  [required]
  --help                Show this message and exit.
```
```commandline
(py8) PS C:\laragon\www\efishery-test-case> python .\main.py pranala get-all-by-range
Please input range price (from,to). Ex. 2000,5000: 2,50000
Please input range size based on option size (from,to). Ex. 30,50: 30,170
Please input range date yyyy-mm-dd (from,to). Ex. 2020-11-02,2022-11-02: 2020-11-02,2022-11-02
                                     uuid komoditas area_provinsi  area_kota size  price  tgl_parsed      timestamp
185  7d53954e-45a5-4a45-9e5c-1660e7847f09    GURAME          ACEH  ACEH KOTA  170  50000  2022-05-09  1652101460443
```

### Get Data Based On Specified Area
You can get data based on specified area province and city using `get-by-area` and it will show a prompt to user to input the province and city.
```commandline
(py8) PS C:\laragon\www\efishery-test-case> python .\main.py pranala get-by-area --help
Usage: main.py pranala get-by-area [OPTIONS]

  get by area province and city

Options:
  --province TEXT  [required]
  --city TEXT      [required]
  --help           Show this message and exit.
```
```commandline
(py8) PS C:\laragon\www\efishery-test-case> python .\main.py pranala get-by-area
Province: jawa tengah
City: cilacap
uuid                                  komoditas    area_provinsi    area_kota      size    price  tgl_parsed                timestamp    no    price_in_usd
------------------------------------  -----------  ---------------  -----------  ------  -------  --------------------  -------------  ----  --------------
03152e70-9c60-4cd7-94ea-e0b71b260bb6  BAWAL        JAWA TENGAH      CILACAP         150    70000  2022-01-28T17:50:58Z  1643392258877     1         4.55771
34fd07a0-1e9a-43c2-872e-85ba67735198  NILA MERAH   JAWA TENGAH      CILACAP         170    96000  2022-02-16T11:49:14Z  1645012154189     2         6.25058
2d812e68-b96a-496f-92df-7a7c363766aa  PATIN        JAWA TENGAH      CILACAP         110    29000  2022-03-07T09:40:52Z  1646646052408     3         1.8882
f9f653e0-23c8-40c0-b852-9553b441c900  PATIN        JAWA TENGAH      CILACAP          20    95000  2022-03-11T15:05:01Z  1647011101686     4         6.18547
275eccdf-e60e-4693-8e20-727beb8faa4d  LELE         JAWA TENGAH      CILACAP          20    83000  2022-03-22T18:17:27Z  1647973047984     5         5.40414
5c58a120-cb23-492a-b38f-76d80f48c62d  LELE         JAWA TENGAH      CILACAP         150    41000  2022-03-25T09:07:37Z  1648199257904     6         2.66952
6ef89150-3ebe-40d9-90f5-1c89dd501cb0  NILA HITAM   JAWA TENGAH      CILACAP          60    81000  2022-04-22T09:05:18Z  1650618318846     7         5.27392
f2012153-75ef-48e5-b40d-b60762771e4b  BAWAL        JAWA TENGAH      CILACAP          20    44000  2022-11-04T15:33:19Z  1667550799938     8         2.86485
79877fd3-1aa7-4b19-ad51-8246a3338b1f  BAWAL        JAWA TENGAH      CILACAP          30    46000  2022-11-04T15:34:24Z  1667550864542     9         2.99507
```

### Get Data Based On Specified Id
You can get data based on specified id using `get-by-id` and it will show a prompt to user to input the id.
```commandline
(py8) PS C:\laragon\www\efishery-test-case> python .\main.py pranala get-by-id --help
Usage: main.py pranala get-by-id [OPTIONS]

  get by uuid

Options:
  --uuid TEXT  [required]
  --help       Show this message and exit.
```
```commandline
(py8) PS C:\laragon\www\efishery-test-case> python .\main.py pranala get-by-id
Uuid: 2c75f19f-ac7a-4c28-9459-8fbb64c8cb00
uuid                                  komoditas    area_provinsi    area_kota      size    price  tgl_parsed                timestamp    no    price_in_usd
------------------------------------  -----------  ---------------  -----------  ------  -------  --------------------  -------------  ----  --------------
2c75f19f-ac7a-4c28-9459-8fbb64c8cb00  GURAME       JAWA TENGAH      PURWOREJOL       40    55000  2022-01-01T13:11:46Z  1641042706799     1         3.58106
```

### Get Data Based On Specified Range Price
You can get data based on specified range price using `get-by-range-price` and it will show a prompt to user to input the start price and end price.
```commandline
(py8) PS C:\case> python .\main.py pranala get-by-range-price --help
Usage: main.py pranala get-by-range-price [OPTIONS]

  get by range price

Options:
  --start-price INTEGER  [required]
  --end-price INTEGER    [required]
  --help                 Show this message and exit.
```
```commandline
(py8) PS C:\case> python .\main.py pranala get-by-range-price
Start price: 50
End price: 5000
uuid                                  komoditas    area_provinsi     area_kota      size    price  tgl_parsed                timestamp    price_in_usd
------------------------------------  -----------  ----------------  -----------  ------  -------  --------------------  -------------  --------------
7ffda1e2-163d-4430-a661-5c29b1eac424  GURAME       JAWA TENGAH       PURWOREJO       110     3000  2022-01-02T01:33:44Z  1641087224309       0.195331
ee5fbdb0-4a78-408e-99d3-4c06ee99643d  PATIN        SUMATERA UTARA    MEDAN           170     3000  2022-01-11T17:41:43Z  1641922903531       0.195331
f1fd3ce3-f003-44d7-a596-11eb3c4f0528  MAS          DKI JAKARTA       KOTA TUA        200     2000  2022-01-12T17:59:34Z  1642010374281       0.13022
52d32684-1d66-47c2-85f5-87a897005ee6  BANDENG      KALIMANTAN TIMUR  BORNEO           40     5000  2022-01-28T05:41:16Z  1643348476148       0.325551
6f6fad5e-1a38-4863-bb1b-a9a8eaa9c6b7  PATIN        BALI              BULELENG         80     1000  2022-02-03T19:14:58Z  1643915698310       0.0651102
9adbd793-4bf4-4ce4-acd7-cd90ab1160bf  BAWAL        JAWA TIMUR        PROBOLINGGO      40     1000  2022-02-17T17:00:37Z  1645117237207       0.0651102
bf766e07-b9d5-44d2-bede-c3ad13a9e246  BAWAL        BANTEN            PANDEGLANG       20     2000  2022-02-23T14:18:02Z  1645625882138       0.13022
625b4673-8795-4b6c-84b5-9e8dcad83485  MAS          JAWA TENGAH       PURWOREJOL      150     1000  2022-03-05T05:26:18Z  1646457978287       0.0651102
```

### Get Max Price Data By Week And By Commodity
You can get max price data using `get-max-price` and it will show data filtered based by week and get the max price of each weeks.
```commandline
(py8) PS C:\laragon\www\efishery-test-case> python .\main.py pranala get-max-price --help
Usage: main.py pranala get-max-price [OPTIONS]

  get max price by week and commodity

Options:
  --help  Show this message and exit.
```
```commandline
(py8) PS C:\laragon\www\efishery-test-case> python .\main.py pranala get-max-price
                                     price
komoditas tgl_parsed
BANDENG   2022-01-03 00:00:00+00:00  91000
          2022-01-17 00:00:00+00:00  84000
          2022-01-24 00:00:00+00:00  73000
          2022-02-07 00:00:00+00:00  41000
          2022-02-14 00:00:00+00:00  97000
...                                    ...
PATIN     2022-04-04 00:00:00+00:00  62000
          2022-04-11 00:00:00+00:00  12000
          2022-04-18 00:00:00+00:00  85000
          2022-04-25 00:00:00+00:00  79000
          2022-05-23 00:00:00+00:00  56000

[118 rows x 1 columns]
```

### Get Most Records Column Data
You can get most records column data using `get-most-records` and it will show you a table with most value based on commodity.
```commandline
(py8) PS C:\laragon\www\efishery-test-case> python .\main.py pranala get-most-records --help
Usage: main.py pranala get-most-records [OPTIONS]

  get most records by commodity

Options:
  --help  Show this message and exit.
```
```commandline
(py8) PS C:\laragon\www\efishery-test-case> python .\main.py pranala get-most-records
BANDENG       43
GURAME        29
PATIN         29
BAWAL         28
MAS           28
NILA HITAM    23
LELE          23
NILA MERAH    17
Name: komoditas, dtype: int64
```

## Documentation Functions

### Get Function
On get function, it uses `session` from `requests_cache` to cache the response into sqlite.

When `params` is exists it will pass it into `session.get` parameter. Then proceed to display the result.

```python
@staticmethod
def get(params=None, context=None, c_value=None):
    """
    get the response with/o params
    """
    if params is not None:
        params = {'search': json.dumps(params)}
    response = session.get(url_list, params=params)
    get_response(response, context, c_value)
```

When the response is ok then we need to check if the response data is exists. After that we need to check is the response coming from `context is not None`.

To display the result of the response, we need to convert it into table, so user can see the data.

`context` is needed to only desired result and not using tabulate to display the data.

`c_value` also is needed when context exists.

```python
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
```

When the `context` is `get_max_price`, dataset is filled with all the list of data from `session.get()`.
Then put it in dataframe from pandas including with keys / headers.
And parse the column `tgl_parsed` with datetime type so we can calculate with datetime type data.
The result will grouped within the lists column of `komoditas`, calculated `tgl_parsed` and max data of `price`

```python
if context == 'get_max_price':
    df = pd.DataFrame(dataset, columns=dataset[0].keys())
    df['tgl_parsed'] = pd.to_datetime(df['tgl_parsed']) - pd.to_timedelta(7, unit='d')
    df = df.groupby(['komoditas', pd.Grouper(key='tgl_parsed', freq='W-MON')]).agg(price = ('price' , 'max')).round()
    print (df)
    return False
```

When the `context` is `get_most_records` the data will be display using `dataframe` from `pandas` and calculate using `value_counts` to count all the value based on desired column.

```python
elif context == 'get_most_records':
    df = pd.DataFrame(dataset, columns=dataset[0].keys())
    result = df['komoditas'].value_counts()
    print (result)
    return False
```

When the `context` is `get_by_range_price` the goals is to display the data based on range data.

`c_value` is inputted user data. And we need to convert the date into datetime type, so it can be check using dataframe.

```python
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
```

### Currecy Converter
Currency converter packages is used to calculate the price and push it into the dictionary.
```python
x['price_in_usd'] = (c.convert(x.get('price'), 'IDR', 'USD'))
```