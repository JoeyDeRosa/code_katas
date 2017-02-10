"""Forbes sorting."""


import json


def forbes():
    """forbes sort."""

    with open('forbes_list.json') as data_list:
        data = data_list.read()

    if data[-3] == ',':
        data = data[:-3] + data[-2:]

    data = json.loads(data)

    oldest_under_80 = data[0]
    youngest = data[0]

    for billionaire in data:
        print(billionaire)
        if billionaire['age'] > oldest_under_80['age'] and billionaire['age'] < 80:
            oldest_under_80 = billionaire
        if billionaire['age'] < youngest['age'] and billionaire['age'] > 0:
            youngest = billionaire

    return('youngest:', 
            youngest['name'], 
            youngest['net_worth (USD)'], 
            youngest['source'], 
            'oldest under 80', 
            oldest_under_80['name'], 
            oldest_under_80['net_worth (USD)'],
            oldest_under_80['source'])