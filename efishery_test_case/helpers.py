import re
import datetime


def format_numbers_only(string):
    """
    remove everything but number
    :param string:
    :return:
    """
    return re.sub(r"\D+", "", string)


def format_letters_only(string):
    """
    remove everything but letters
    :param string:
    :return:
    """
    return re.sub(r"[^a-zA-Z]+", "", string)


def validate_tanggal(date):
    """
    validate format date
    :param date:
    :return:
    """
    try:
        datetime_str = date
        datetime_object = datetime.datetime.strptime(datetime_str, '%Y-%m-%d').date()
        return str(datetime_object)
    except ValueError:
        return False


def normalized_input(input):
    try:
        rinput = {}
        for x in input:
            cdata = x.split(',')
            for y in cdata:
                rdata = y.split('=')
                rinput[rdata[0]] = rdata[1]
        return rinput
    except IndexError:
        return False
    except ValueError:
        return False
    except TypeError:
        return False
