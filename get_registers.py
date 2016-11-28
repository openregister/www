import requests


def get_all_registers(base_url):
    url = "http://register.{}/records.json?page-size=5000".format(base_url)
    data = {
        'base_url': base_url,
        'item_list': requests.get(url).json()
    }
    return data
