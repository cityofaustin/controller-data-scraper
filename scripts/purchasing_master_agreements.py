'''
Scrape master agreements from COA Controller webpage and upload to staging database.
'''
import csv
import os
import pdb

from bs4 import BeautifulSoup
import requests

from config import *
from utils import *



def get_html(url, dept=2400):
    form_data = {'selauth' : dept}
    res = requests.post(url, data=form_data)
    res.raise_for_status()
    return res.text


def handle_html(html):
    soup = BeautifulSoup(html, "html.parser")
    rows = soup.find_all('tr')
    rows = rows[9:]

    parsed = []

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        parsed.append(cols)

    return parsed


def handle_rows(fieldnames=None, rows=None):
     return [dict(zip(fieldnames, row)) for row in rows]
     

def main():
    html = get_html(MASTER_AGREEMENTS_ENDPOINT)
    
    rows = handle_html(html)
    
    fieldnames = rows.pop(0)
    
    data = handle_rows(fieldnames=fieldnames, rows=rows)

    filename = outpath('master_agreements.csv', 'data')
    
    return to_csv(data, fieldnames=fieldnames, filename=filename)


if __name__=='__main__':
    
    try:
        results = main()

    except Exception as e:        
        raise e















