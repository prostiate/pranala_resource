import typer
import requests
import uuid
from typing import List, Optional
from requests_cache import CachedSession
from datetime import timedelta, datetime
from efishery_test_case.response import *
from efishery_test_case.helpers import *

url = 'https://stein.efishery.com/v1/storages/5e1edf521073e315924ceab4/list'


class Pranala:  # noqa
    app = typer.Typer()

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
        # print('url: ', url)
        if params is not None:
            params = {'search': json.dumps(params)}
        response = session.get(url, params=params)
        # print('params: ', params)
        # print('response.url: ', response.url)
        get_response(response, context, c_value)

    @staticmethod
    @app.command()
    def get_all_by_range(
            harga: str = typer.Option(..., prompt=True),
            size: str = typer.Option(..., prompt=True),
            tanggal: str = typer.Option(..., prompt=True)
    ):
        """
        get all by harga, size and tanggal
        """
        params = dict()
        params['harga'] = format_numbers_only(harga)
        params['size'] = format_numbers_only(str(size))
        params['tgl_parsed'] = validate_tanggal(tanggal)
        return Pranala.get(params)

    @staticmethod
    @app.command()
    def get_all_by_commodity(komoditas: str = typer.Option(..., prompt=True)):
        """
        get all by commodity
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
    def get_by_area_provinsi(provinsi: str = typer.Option(..., prompt=True)):
        """
        get by area provinsi
        """
        params = dict()
        if provinsi:
            params['area_provinsi'] = str(provinsi).upper()
        return Pranala.get(params)

    @staticmethod
    @app.command()
    def get_by_area_kota(kota: str = typer.Option(..., prompt=True)):
        """
        get by area kota
        """
        params = dict()
        params['area_kota'] = str(kota).upper()
        return Pranala.get(params)

    @staticmethod
    @app.command()
    def get_max_price(komoditas: str = typer.Option(..., prompt=True)):
        """
        get max price by commodity
        """
        params = dict()
        params['komoditas'] = str(komoditas).upper()
        return Pranala.get(params, 'get_max_price')

    @staticmethod
    @app.command()
    def get_most_records(by: str = typer.Option(..., prompt=True)):
        """
        get most records by commodity column
        """
        return Pranala.get(context='get_most_records', c_value=by)

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

    @staticmethod
    def post(data):
        # print('def post data:', data)
        if data is None:
            return 'data is required'
        # response = requests.post(self.url, data='[{"komoditas":"hehe"}]', headers={'Content-Type': 'application/json'})
        response = requests.post(
            url,
            data=json.dumps(data),
            headers={'Content-Type': 'application/json'})
        simple_response(response, 'data successfully created')

    @staticmethod
    def put(condition, set_value):
        if condition is None or set_value is None:
            return 'condition and set_value is required'
            raise typer.Abort()

        data = json.dumps({"condition": condition, "set": set_value})
        # print('def update')
        # print(data)
        response = requests.put(
            url,
            data=data,
            headers={'Content-Type': 'application/json'}
        )
        simple_response(response, 'date successfully updated')

    @staticmethod
    def delete(condition):
        if condition is None:
            return 'condition is required'
        data = json.dumps({"condition": condition})
        # print('def delete')
        # print(data)
        response = requests.delete(
            url,
            data=data,
            headers={'Content-Type': 'application/json'}
        )
        simple_response(response, 'data successfully deleted')

    @staticmethod
    @app.command()
    def add_records(
            komoditas: str = typer.Option(..., prompt=True),
            area_provinsi: str = typer.Option(..., prompt=True),
            area_kota: str = typer.Option(..., prompt=True),
            size: int = typer.Option(..., prompt=True),
            price: int = typer.Option(..., prompt=True),
    ):
        """
        This command to add a record, and it will ask you to input required data
        """
        date = datetime.datetime.timestamp(datetime.datetime.now())*1000
        data = [{
            "uuid": str(uuid.uuid4()),
            "komoditas": str(komoditas).upper(),
            "area_provinsi": str(area_provinsi).upper(),
            "area_kota": str(area_kota).upper(),
            "size": format_numbers_only(str(size)),
            "price": format_numbers_only(str(price)),
            "tgl_parsed": datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
            "timestamp": round(date)
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

        rcondition = normalized_condition(condition)
        if not rcondition:
            print("Wrong format on --condition! Example: --condition uuid=123,komoditas=GURAME")
            raise typer.Abort()

        rset_value = normalized_set_value(set_value)
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

        rcondition = normalized_condition(condition)
        if not rcondition:
            print("Wrong format on --condition! Example: --condition uuid=123,komoditas=GURAME")
            raise typer.Abort()

        if action:
            print("Deleting...")
            return Pranala.delete(rcondition)
        else:
            print("Operation cancelled")
