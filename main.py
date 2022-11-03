from efishery_test_case import Pranala
import typer

app = typer.Typer()
app.add_typer(Pranala.app, name='pranala')

if __name__ == '__main__':
    app()

# if __name__ == '__main__':
# url = 'https://stein.efishery.com/v1/storages/5e1edf521073e315924ceab4/list?search={"komoditas":"GURAME","uuid":"2c75f19f-ac7a-4c28-9459-8fbb64c8cb00","area_provinsi":"JAWA TENGAH"}'
# url = 'https://stein.efishery.com/v1/storages/5e1edf521073e315924ceab4/list?search={"tgl_parsed":"2022-01-04T00:00:00Z"}'
# url = 'https://stein.efishery.com/v1/storages/5e1edf521073e315924ceab4/list'
# url = 'https://api.steinhq.com/v1/storages/5cc158079ec99a2f484dcb40/Sheet1'
# pranala = Pranala(url) # noqa
# pranala.get()
# pranala.get_all_by_range()
# pranala.get_all_by_commodity(komoditas='gurame')
# pranala.get_by_id('6f57732f-9a26-4e0e-8152-abacba6c5cdd')
# pranala.get_by_area('JAWA BARAT')

# range nanti ini dibikin based on length yang diinput oleh user
# data = [{"komoditas": "test"} for _ in range(1)]
# pranala.add_records(data)

# condition = {"komoditas": 'hehe'}
# set_value = {"uuid": str(uuid.uuid4()), "area_provinsi": "JAWA BARAT"}
# pranala.update_records(condition, set_value)

# data = {"komoditas": "test"}
# pranala.delete_records(data)
