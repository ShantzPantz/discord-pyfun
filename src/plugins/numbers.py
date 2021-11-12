'''
    Number facts!
    Usage:
    !numbers [number]
    !numbers [number] [type]
    valid types are "trivia, math, date, year"
    ** Date are month and day, formatted as 3/27 ex: !numbers 3/27
'''

import random
from datetime import date

import requests

__author__ = ('Brian', 'Shantz')
COMMAND = 'numbers'


def api_request(number, type):
    url = "http://numbersapi.com/{}/{}".format(number, type)
    return requests.get(url)


def is_date_request(parts):
    if len(parts) == 1 and parts[0] == "today":
        number = date.today().strftime('%m/%d')
        return True, number
    elif len(parts) == 1:
        if "/" in parts[0]:
            return True, parts[0]
    elif len(parts) == 2:
        if "/" in parts[0] and parts[1] == "date":
            return True, parts[0]
        elif "/" in parts[1] and parts[0] == "date":
            return True, parts[1]
        else:
            return False, None
    else:
        return False, None


def is_trivia_request(parts):
    if len(parts) == 1:
        try:
            number = int(parts[0])
            return True, number
        except ValueError:
            return False, None
    elif len(parts) == 2:
        if parts[0] == "trivia":
            return True, parts[1]
        elif parts[1] == "trivia":
            return True, parts[0]
        else:
            return False, None
    else:
        return False, None


def is_math_request(parts):
    if len(parts) == 2:
        if parts[0] == "math":
            return True, parts[1]
        elif parts[1] == "math":
            return True, parts[0]
        else:
            return False, None
    else:
        return False, None

def is_year_request(parts):
    if len(parts) == 2:
        if parts[0] == "year":
            return True, parts[1]
        elif parts[1] == "year":
            return True, parts[0]
        else:
            return False, None
    else:
        return False, None

async def send_response(channel, r):
    if r.ok:
        await channel.send(r.text)
    else:
        await channel.send("Request to numbersapi failed with status code: {}".format(r.status_code))

async def main(bot, message, **kwargs):
    command_types = ["date", "trivia", "math", "year"]
    # split commands up
    parts = message.content.split(' ')

    yesno, number = is_year_request(parts)
    if yesno:
        r = api_request(number, "year")
        await send_response(message.channel, r)
        return

    yesno, number = is_trivia_request(parts)
    if yesno:
        r = api_request(number, "trivia")
        await send_response(message.channel, r)
        return

    yesno, number = is_date_request(parts)
    if yesno:
        r = api_request(number, "date")
        await send_response(message.channel, r)
        return

    yesno, number = is_math_request(parts)
    if yesno:
        r = api_request(number, "math")
        await send_response(message.channel, r)
        return

