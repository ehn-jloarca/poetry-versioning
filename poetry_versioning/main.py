import pytz
import random

import requests


def foo():
    return 'bar'


def get_time(timezone):
    """
    Get the current time in a timezone

    :param timezone: timezone name
    :return: dict with date and time in the specified timezone
    """
    payload = {'timeZone': timezone}
    r = requests.get('https://www.timeapi.io/api/Time/current/zone', params=payload)
    resp = r.json()

    return {'timezone': timezone, 'date': resp['date'], 'time': resp['time']}


def find_random_timezone():
    """
    Find and return a random timezone using pytz

    :return: timezone name (IANA)
    """
    return random.choice(pytz.all_timezones)
