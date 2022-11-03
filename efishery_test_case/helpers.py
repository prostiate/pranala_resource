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
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


def normalized_condition(condition):
    try:
        rcondition = {}
        for x in condition:
            cdata = x.split(',')
            for y in cdata:
                rdata = y.split('=')
                rcondition[rdata[0]] = rdata[1]
        return rcondition
    except IndexError:
        return False
    except ValueError:
        return False
    except TypeError:
        return False


def normalized_set_value(set_value):
    try:
        rset_value = {}
        for x in set_value:
            cdata = x.split(',')
            for y in cdata:
                rdata = y.split('=')
                rset_value[rdata[0]] = rdata[1]
        return rset_value
    except IndexError:
        return False
    except ValueError:
        return False
    except TypeError:
        return False
