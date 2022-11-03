# Pranala Resources CLI and Wrapper
Pranala Resource is a library with build-in CLI application that users will can interact. Based on Python 3.8+.

Typer is used to build CLI application. 

List of commands:
- add-records: Create a new record and there will be prompt to input the data
- delete-records: Update a record based on condition with the values of condition and set-value.
- get-aggregation-price: get aggregation price by the specified column
- get-all-by-commodity: get all data by commodity column
- get-all-by-range: get all data by harga, size and tanggal
- get-by-area-kota: get by area kota
- get-by-area-provinsi: get data by area provinsi
- get-by-id: get by uuid
- get-by-range-price: get by range price
- get-max-price: get max price by commodity
- get-most-records: get most records by commodity
- update-records: Update records with condition and value.

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
  add-records            This command to add a record, and it will ask...
  delete-records         Update records with condition and value.
  get-aggregation-price  get aggregation price by the specified column
  get-all-by-commodity   get all by commodity
  get-all-by-range       get all by harga, size and tanggal
  get-by-area-kota       get by area kota
  get-by-area-provinsi   get by area provinsi
  get-by-id              get by uuid
  get-by-range-price     get by range price
  get-max-price          get max price by commodity
  get-most-records       get most records by commodity column
  update-records         Update records with condition and value.
```

### Add a record
You can add a record using `add-records` and then it will show prompt. You can use `--help` arguments to see requirements input.
```commandline
(py8) PS C:\case> python .\main.py pranala add-records --help
Usage: main.py pranala add-records [OPTIONS]

  This command to add a record, and it will ask you to input required data

Options:
  --komoditas TEXT      [required]
  --area-provinsi TEXT  [required]
  --area-kota TEXT      [required]
  --size INTEGER        [required]
  --price INTEGER       [required]
  --help                Show this message and exit.
```
```commandline
(py8) PS C:\case> python .\main.py pranala add-records
Komoditas: GURAME
Area provinsi: JAWA BARAT
Area kota: BANDUNG
Size: 100
Price: 50000
data successfully created
```

### Update a record
You can update a record using `update-records` and you need to use `--condition condition1=value1,condition2=value2 --set-value column1=value1,column2=value2` in order to update the data.
```commandline
(py8) PS C:\case> python .\main.py pranala update-records --help
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
(py8) PS C:\case> python .\main.py pranala update-records --condition uuid=2c75f19f-ac7a-4c28-9459-8fbb64c8cb00 --set-value komoditas=GURAME
condition:  {'uuid': '2c75f19f-ac7a-4c28-9459-8fbb64c8cb00'}
set_value:  {'komoditas': 'GURAME'}
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
(py8) PS C:\case> python .\main.py pranala get-all-by-commodity --help
Usage: main.py pranala get-all-by-commodity [OPTIONS]

  get all by commodity

Options:
  --komoditas TEXT  [required]
  --help            Show this message and exit.
```
```commandline
(py8) PS C:\case> python .\main.py pranala get-all-by-commodity
Komoditas: GURAME
uuid                                  komoditas    area_provinsi     area_kota          size    price  tgl_parsed                timestamp    price_in_usd
------------------------------------  -----------  ----------------  ---------------  ------  -------  --------------------  -------------  --------------
2c75f19f-ac7a-4c28-9459-8fbb64c8cb00  GURAME       JAWA TENGAH       PURWOREJOL           40    55000  2022-01-01T13:11:46Z  1641042706799        3.58106
b175e2c0-a97e-4cf4-b16f-ab8f59c1a429  GURAME       KALIMANTAN TIMUR  BORNEO               30    87000  2022-01-01T23:34:16Z  1641080056368        5.66459
7ffda1e2-163d-4430-a661-5c29b1eac424  GURAME       JAWA TENGAH       PURWOREJO           110     3000  2022-01-02T01:33:44Z  1641087224309        0.195331
9210ca57-b15f-431f-9135-67126dd7c6f0  GURAME       JAWA TIMUR        BANYUWANGI          130    73000  2022-02-02T16:25:38Z  1643819138296        4.75304
6c8bfe30-ded7-4b6b-bdaf-1b5f3ea33cbd  GURAME       JAWA BARAT        CIMAHI              200    96000  2022-02-10T00:38:55Z  1644453535618        6.25058
eb353254-49cb-49a2-900e-43da80cfa2f7  GURAME       JAWA TENGAH       PURWOREJOR          110    57000  2022-02-10T08:44:37Z  1644482677674        3.71128
c7b0d94c-553d-49c7-91d1-6ffbb59b872a  GURAME       JAWA TIMUR        PROBOLINGGO          60    38000  2022-02-12T08:48:20Z  1644655700611        2.47419
6f57732f-9a26-4e0e-8152-abacba6c5cdd  GURAME       JAWA TENGAH       TEGAL               160    69000  2022-02-18T05:50:20Z  1645163420277        4.4926
```

### Get All Data Based On Specified Price, Size And Date
You can get all data based on specified price, size and date using `get-all-by-range` and it will show a prompt to user to input the price, size and date.
```commandline
(py8) PS C:\case> python .\main.py pranala get-all-by-range --help
Usage: main.py pranala get-all-by-range [OPTIONS]

  get all by harga, size and tanggal

Options:
  --harga TEXT    [required]
  --size TEXT     [required]
  --tanggal TEXT  [required]
  --help          Show this message and exit.
```
```commandline
(py8) PS C:\case> python .\main.py pranala get-all-by-commodity
Harga: 55000
Size: 10
Tanggal: 2022-01-01
uuid                                  komoditas    area_provinsi     area_kota          size    price  tgl_parsed                timestamp    price_in_usd
------------------------------------  -----------  ----------------  ---------------  ------  -------  --------------------  -------------  --------------
2c75f19f-ac7a-4c28-9459-8fbb64c8cb00  GURAME       JAWA TENGAH       PURWOREJOL           10    55000  2022-01-01T13:11:46Z  1641042706799        3.58106
```

### Get Data Based On Specified Area Kota
You can get data based on specified area kota using `get-by-area-kota` and it will show a prompt to user to input the kota name.
```commandline
(py8) PS C:\case> python .\main.py pranala get-by-area-kota --help
Usage: main.py pranala get-by-area-kota [OPTIONS]

  get by area kota

Options:
  --kota TEXT  [required]
  --help       Show this message and exit.
```
```commandline
(py8) PS C:\case> python .\main.py pranala get-by-area-kota
Kota: BANDUNG
uuid                                  komoditas    area_provinsi    area_kota      size    price  tgl_parsed                timestamp    price_in_usd
------------------------------------  -----------  ---------------  -----------  ------  -------  --------------------  -------------  --------------
f34724d0-82e8-4e2c-96ac-e67d89c2d98f  NILA HITAM   JAWA BARAT       BANDUNG          90    50000  2022-01-27T11:33:17Z  1643283197156         3.25551
c2418c63-9b9f-4575-a55d-03087fabb49a  LELE         JAWA BARAT       BANDUNG          50    79000  2022-03-24T09:20:10Z  1648113610478         5.1437
2ac035bc-69ca-4d80-be1f-398f5a2ba29a  NILA MERAH   JAWA BARAT       BANDUNG         140    62000  2022-05-13T02:48:45Z  1652410125334         4.03683
85306e0c-12da-45e0-99d9-149a4ba432b8  GURAME       JAWA BARAT       BANDUNG          50    35000  2022-05-28T04:45:25Z  1653713125390         2.27886
```

### Get Data Based On Specified Area Provinsi
You can get data based on specified area provinsi using `get-by-area-provinsi` and it will show a prompt to user to input the provinsi name.
```commandline
(py8) PS C:\case> python .\main.py pranala get-by-area-provinsi --help
Usage: main.py pranala get-by-area-provinsi [OPTIONS]

  get by area provinsi

Options:
  --provinsi TEXT  [required]
  --help           Show this message and exit.
```
```commandline
(py8) PS C:\case> python .\main.py pranala get-by-area-provinsi
Provinsi: JAWA TENGAH
uuid                                  komoditas    area_provinsi    area_kota      size    price  tgl_parsed                timestamp    price_in_usd
------------------------------------  -----------  ---------------  -----------  ------  -------  --------------------  -------------  --------------
2c75f19f-ac7a-4c28-9459-8fbb64c8cb00  GURAME       JAWA TENGAH      PURWOREJOL       40    55000  2022-01-01T13:11:46Z  1641042706799       3.58106
7ffda1e2-163d-4430-a661-5c29b1eac424  GURAME       JAWA TENGAH      PURWOREJO       110     3000  2022-01-02T01:33:44Z  1641087224309       0.195331
1f9a1f94-bf3f-4e9d-b13f-d5f83bc1ef7e  NILA HITAM   JAWA TENGAH      TEGAL           150    59000  2022-01-04T15:33:43Z  1641310423170       3.8415
ae0d90d6-26ea-4047-a605-9ce36c302f09  NILA MERAH   JAWA TENGAH      PURWOREJO       100    28000  2022-01-07T13:23:45Z  1641561825476       1.82308
c10dbca7-1e90-4255-8294-06ff2a13509d  BANDENG      JAWA TENGAH      PURWOREJO       100    91000  2022-01-07T16:16:37Z  1641572197343       5.92503
92228d24-e61f-4abc-a5d3-3f0d17db5820  MAS          JAWA TENGAH      PURWOREJO       180    14000  2022-01-11T16:35:03Z  1641918903712       0.911542
54d6a2fa-8c03-4459-b45c-47fa58fb0934  MAS          JAWA TENGAH      PURWOREJO        30    61000  2022-01-16T17:42:15Z  1642354935189       3.97172
```

### Get Data Based On Specified Id
You can get data based on specified id using `get-by-id` and it will show a prompt to user to input the id.
```commandline
(py8) PS C:\case> python .\main.py pranala get-by-id --help
Usage: main.py pranala get-by-id [OPTIONS]

  get by uuid

Options:
  --uuid TEXT  [required]
  --help       Show this message and exit.
```
```commandline
(py8) PS C:\case> python .\main.py pranala get-by-id
Uuid: 54d6a2fa-8c03-4459-b45c-47fa58fb0934
uuid                                  komoditas    area_provinsi    area_kota      size    price  tgl_parsed                timestamp    price_in_usd
------------------------------------  -----------  ---------------  -----------  ------  -------  --------------------  -------------  --------------
54d6a2fa-8c03-4459-b45c-47fa58fb0934  MAS          JAWA TENGAH      PURWOREJO        30    61000  2022-01-16T17:42:15Z  1642354935189         3.97172
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

### Get Max Price Data Based On Commodity Column Value
You can get max price data based on specified column commodity value using `get-max-price` and it will show a prompt to user to input the commodity value.
```commandline
(py8) PS C:\case> python .\main.py pranala get-max-price --help
Usage: main.py pranala get-max-price [OPTIONS]

  get max price by commodity

Options:
  --komoditas TEXT  [required]
  --help            Show this message and exit.
```
```commandline
(py8) PS C:\case> python .\main.py pranala get-max-price
Komoditas: GURAME
uuid                                  komoditas    area_provinsi     area_kota          size    price  tgl_parsed                timestamp    price_in_usd
------------------------------------  -----------  ----------------  ---------------  ------  -------  --------------------  -------------  --------------
6c8bfe30-ded7-4b6b-bdaf-1b5f3ea33cbd  GURAME       JAWA BARAT        CIMAHI              200    96000  2022-02-10T00:38:55Z  1644453535618        6.25058
c4f6ed2f-a4a3-4773-b712-e514f4182be9  GURAME                                             120    90000  2022-01-16T06:22:46Z  1642314166739        5.85992
5379e93e-68c7-408e-b11b-8aa32c33376d  GURAME       JAWA TIMUR        SITUBONDO           100    89000  2022-05-09T22:07:55Z  1652134075533        5.79481
1e271943-ff69-4f18-b94c-0de4b979e78c  GURAME       JAWA TIMUR        BANYUWANGI          180    88000  2022-05-05T23:39:58Z  1651793998375        5.7297
b175e2c0-a97e-4cf4-b16f-ab8f59c1a429  GURAME       KALIMANTAN TIMUR  BORNEO               30    87000  2022-01-01T23:34:16Z  1641080056368        5.66459
76291afa-e1f5-4244-b7fb-bd6fcf3b8f1a  GURAME       JAWA TIMUR        SITUBONDO           180    87000  2022-02-28T01:03:37Z  1646010217928        5.66459
8e14a80b-05b4-4833-8870-32022c97bc07  GURAME       ACEH              ACEH KOTA           140    86000  2022-03-17T10:46:44Z  1647514004186        5.59948
```

### Get Most Records Column Data
You can get most records column data using `get-most-records` and it will show a prompt to user to input the column name.
```commandline
(py8) PS C:\case> python .\main.py pranala get-most-records --help
Usage: main.py pranala get-most-records [OPTIONS]

  get most records by commodity column

Options:
  --by TEXT  [required]
  --help     Show this message and exit.
```
```commandline
(py8) PS C:\case> python .\main.py pranala get-most-records
By: komoditas
  GURAME    NILA HITAM    LELE    BAWAL    BANDENG    NILA MERAH    MAS    PATIN    None    Komoditas    Sss
--------  ------------  ------  -------  ---------  ------------  -----  -------  ------  -----------  -----
      29            23      23       26         43            17     28       29       1            1     41
```

## Documentation Functions

### Get Function
On get function, it uses requests_cache to cache the response into sqlite and if the response is ok then it will show the data.
```python
    @staticmethod
    def get(params=None, context=None, c_value=None):
        """
        get the response with/o params
        """
        session = CachedSession(
            'pranala_cache',
            use_cache_dir=True,  # Save files in the default user cache dir
            cache_control=True,  # Use Cache-Control headers for expiration, if available
            expire_after=timedelta(days=1),  # Otherwise expire responses after one day
            allowable_methods=['GET', 'POST'],  # Cache POST requests to avoid sending the same data twice
            allowable_codes=[200, 400],  # Cache 400 responses as a solemn reminder of your failures
            ignored_parameters=['api_key'],  # Don't match this param or save it in the cache
            match_headers=True,  # Match all request headers
            stale_if_error=True,  # In case of request errors, use stale cache data if possible
        )
        if params is not None:
            params = {'search': json.dumps(params)}
        response = session.get(url, params=params) # call response cache
        get_response(response, context, c_value) # normalized responses
```
When the response is ok then we need to check if the response data is exists. After that we need to check is the response coming from `context is not None`.

```python
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
```

If the `context` is from `get_max_price` then it will sort the price and the data is already filtered on the requests. And it will print the dataset with tabulate function.
```python
if context == 'get_max_price':
    dataset = sorted(dataset, key=lambda d: d['price'], reverse=True)
```

If the `context` is from `get_most_records` then it will count the common values of each list in dictionaries. And it will print the dataset with tabulate function.
```python
elif context == 'get_most_records':
    receivers = [d[c_value] for d in dataset]
    counter = [dict(Counter(receivers))]
    dataset = sorted(counter, key=lambda d: d, reverse=True)
```

If the `context` is from `get_aggregation_price` then it will call pandas to get aggregation functions and using data frame to show the result. And we need to return False because we don't want to call the dataset print function below.
```python
elif context == 'get_aggregation_price':
    dataset[:] = [d for d in dataset if str(d.get('price')).isdigit()]
    df = pd.DataFrame(dataset, columns=dataset[0].keys())
    result = df.groupby(c_value).agg({"price": ['min', 'max']})
    print(result)
    return False
```

If the `context` is from `get_by_range_price` then it will check is price is string with numbers and the price is within the range.
```python
elif context == 'get_aggregation_price':
    dataset[:] = [d for d in dataset if str(d.get('price')).isdigit() and c_value[0] <= int(d.get('price')) <= c_value[1]]
```

### Currecy Converter
Currency converter packages is used to calculate the price and push it into the dictionary.
```python
x['price_in_usd'] = (c.convert(x.get('price'), 'IDR', 'USD'))
```