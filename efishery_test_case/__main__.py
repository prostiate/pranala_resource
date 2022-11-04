import typer
import uuid
from typing import List, Optional
from requests_cache import CachedSession
from datetime import timedelta, datetime
from efishery_test_case.response import *
from efishery_test_case.helpers import *

url_list = 'https://stein.efishery.com/v1/storages/5e1edf521073e315924ceab4/list'
url_option_area = 'https://stein.efishery.com/v1/storages/5e1edf521073e315924ceab4/option_area'
url_option_size = 'https://stein.efishery.com/v1/storages/5e1edf521073e315924ceab4/option_size'

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

class Pranala:  # noqa
    app = typer.Typer()

    @staticmethod
    def get(params=None, context=None, c_value=None):
        """
        get the response with/o params
        """
        if params is not None:
            params = {'search': json.dumps(params)}
        response = session.get(url_list, params=params)
        get_response(response, context, c_value)
        
    @staticmethod
    def get_options(url_option, print = None):
        """
        get option area / size
        """
        if print:
            get_option_response(session.get(url_option))
        else:
            return session.get(url_option)

    @staticmethod
    @app.command()
    def get_all_by_range(
            range_harga: str = typer.Option(..., prompt="Please input range price (from,to). Ex. 2000,5000"),
            range_size: str = typer.Option(..., prompt="Please input range size based on option size (from,to). Ex. 30,50"),
            range_tanggal: str = typer.Option(..., prompt="Please input range date yyyy-mm-dd (from,to). Ex. 2020-11-02,2022-11-02"),
    ):
        """
        get all by range harga, size and tanggal
        """
        option = json.loads(Pranala.get_options(url_option_size).text)

        split_range_harga = range_harga.split(',')
        if "," not in range_harga or len(split_range_harga) > 2:
            print('range price must be: from,to')
            raise typer.Abort()

        split_range_size = range_size.split(',')
        if "," not in range_size or len(split_range_size) > 2:
            print('range size must be: from,to')
            raise typer.Abort()

        split_range_tanggal = range_tanggal.split(',')
        if "," not in range_tanggal or len(split_range_tanggal) > 2:
            print('range date must be: from,to')
            raise typer.Abort()

        if not any(d['size'] == split_range_size[0] for d in option):
            print('Inputted size is not available, please check below:')
            Pranala.get_options(url_option_size, print=True)
            raise typer.Abort()
        
        if validate_tanggal(split_range_tanggal[0]) is False or validate_tanggal(split_range_tanggal[1]) is False:
            print("Incorrect date format, should be YYYY-MM-DD")
            raise typer.Abort()

        return Pranala.get(context='get_all_by_range', c_value=[split_range_harga, split_range_size, split_range_tanggal])

    @staticmethod
    @app.command()
    def get_all_by_commodity(komoditas: str = typer.Option(..., prompt=True)):
        """
        get by commodity
        """
        params = dict()
        params['komoditas'] = str(komoditas).upper()
        return Pranala.get(params)

    @staticmethod
    @app.command()
    def get_by_id(uuid: str = typer.Option(..., prompt=True)):
        """
        get by uuid
        """
        params = dict()
        params['uuid'] = str(uuid)
        return Pranala.get(params)

    @staticmethod
    @app.command()
    def get_by_area(
        province: str = typer.Option(..., prompt=True),
        city: str = typer.Option(..., prompt=True)
    ):
        """
        get by area province and city
        """
        option = json.loads(Pranala.get_options(url_option_area).text)

        province = str(province).upper()
        city = str(city).upper()

        if not any(d['province'] == province and d['city'] == city for d in option):
            print('Inputted province / city is not available, please check below:')
            Pranala.get_options(url_option_area, print=True)
            raise typer.Abort()
        
        params = dict()
        params['area_provinsi'] = province
        params['area_kota'] = city
        return Pranala.get(params)

    @staticmethod
    @app.command()
    def get_max_price():
        """
        get max price by week and commodity
        """
        return Pranala.get(context='get_max_price')

    @staticmethod
    @app.command()
    def get_most_records():
        """
        get most records by commodity
        """
        return Pranala.get(context='get_most_records')

    @staticmethod
    def post(data):
        if data is None:
            return 'data is required'
        response = session.post(
            url_list,
            data=json.dumps(data),
            headers={'Content-Type': 'application/json'})
        simple_response(response, session, 'data successfully created')

    @staticmethod
    def put(condition, set_value):
        if condition is None or set_value is None:
            print('condition and set_value is required')
            raise typer.Abort()

        data = json.dumps({"condition": condition, "set": set_value})
        response = session.put(
            url_list,
            data=data,
            headers={'Content-Type': 'application/json'}
        )
        simple_response(response, session, 'date successfully updated')

    @staticmethod
    def delete(condition):
        if condition is None:
            return 'condition is required'
        data = json.dumps({"condition": condition})
        response = session.delete(
            url_list,
            data=data,
            headers={'Content-Type': 'application/json'}
        )
        simple_response(response, session, 'data successfully deleted')

    @staticmethod
    @app.command()
    def add_records(
            commodity: str = typer.Option(..., prompt=True),
            province: str = typer.Option(..., prompt=True),
            city: str = typer.Option(..., prompt=True),
            size: str = typer.Option(..., prompt=True),
            price: str = typer.Option(..., prompt=True),
    ):
        """
        Add a record
        """
        option = json.loads(Pranala.get_options(url_option_area).text)

        province = str(province).upper()
        city = str(city).upper()

        if not any(d['province'] == province and d['city'] == city for d in option):
            print('Inputted province / city is not available, please check below:')
            Pranala.get_options(url_option_area, print=True)
            raise typer.Abort()

        data = [{
            "uuid": str(uuid.uuid4()),
            "komoditas": str(commodity).upper(),
            "area_provinsi": province,
            "area_kota": city,
            "size": format_numbers_only(size),
            "price": format_numbers_only(price),
            "tgl_parsed": datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
            "timestamp": round(datetime.datetime.timestamp(datetime.datetime.now())*1000)
        } for _ in range(1)]
        return Pranala.post(data)

    @staticmethod
    @app.command()
    def update_records(
            condition: Optional[List[str]] = typer.Option(None),
            set_value: Optional[List[str]] = typer.Option(None),
    ):
        """
        Update records with condition and value. Example:
        --condition uuid=123,komoditas=GURAME
        --set-value komoditas=GURAME,area_provinsi=JAWA BARAT
        """
        if not condition:
            print("--condition is required at least one")
            raise typer.Abort()

        if not set_value:
            print("--set-value is required at least one")
            raise typer.Abort()

        rcondition = normalized_input(condition)
        if not rcondition:
            print("Wrong format on --condition! Example: --condition uuid=123,komoditas=GURAME")
            raise typer.Abort()

        rset_value = normalized_input(set_value)
        if not rset_value:
            print("Wrong format on --set-value! Example: --set-value komoditas=GURAME,area_provinsi=JAWA BARAT")
            raise typer.Abort()

        print('condition: ', rcondition)
        print('set_value: ', rset_value)

        return Pranala.put(rcondition, rset_value)

    @staticmethod
    @app.command()
    def delete_records(
            condition: Optional[List[str]] = typer.Option(None),
            action: bool = typer.Option(..., prompt="Are you sure you want to delete the record?")
    ):
        """
        Update records with condition and value. Example:
        --condition uuid=123,komoditas=GURAME
        """
        if not condition:
            print("--condition is required at least one")
            raise typer.Abort()

        rcondition = normalized_input(condition)
        if not rcondition:
            print("Wrong format on --condition! Example: --condition uuid=123,komoditas=GURAME")
            raise typer.Abort()

        if action:
            print("Deleting...")
            return Pranala.delete(rcondition)
        else:
            print("Operation cancelled")

    @staticmethod
    @app.command()
    def get_aggregation_price(by: str = typer.Option(..., prompt=True)):
        """
        get aggregation price by the specified column
        """
        return Pranala.get(context='get_aggregation_price', c_value=by)

    @staticmethod
    @app.command()
    def get_by_range_price(
            start_price: int = typer.Option(..., prompt=True),
            end_price: int = typer.Option(..., prompt=True)
    ):
        """
        get by range price
        """
        return Pranala.get(context='get_by_range_price', c_value=[start_price, end_price])
