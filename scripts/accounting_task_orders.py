'''
Scrape task orders from COA Controller webpage and upload to Data Tracker.
'''
import csv
import os
import pdb

from bs4 import BeautifulSoup
import requests

from config import *
from utils import *


def get_html(url):
    form_data = {'DeptNumber' : 2400, 'Search': 'Search', 'TaskOrderName': ''}
    res = requests.post(url, data=form_data)
    res.raise_for_status()
    return res.text


def handle_html(html):
    soup = BeautifulSoup(html, "html.parser")
    rows = soup.find_all('tr')
    
    parsed = []

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        parsed.append(cols)

    return parsed


def handle_rows(rows, fieldnames=[]):
    return [dict(zip(fieldnames, row)) for row in rows if len(row)==4]



def main():
    fieldnames=['DEPT', 'TASK_ORDER', 'NAME', 'ACTIVE']

    html = get_html(TASK_ORDERS_ENDPOINT)
    rows = handle_html(html)
    data = handle_rows(rows, fieldnames=fieldnames)

    filename = outpath('task_orders.csv', 'data')
    
    return to_csv(data, fieldnames=fieldnames, filename=filename)

    return len(rows)


if __name__=='__main__':
    
    try:
        results = main()
    

    except Exception as e:        


        raise e















