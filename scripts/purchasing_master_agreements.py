'''
Scrape master agreements from COA Controller webpage and upload to staging database.
'''
import pdb

from bs4 import BeautifulSoup
import requests

from config import *


def to_csv(rows, fieldnames=[], filename='data.csv', header=True):
    with open(filename, 'w', newline='\n') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        if header:
            writer.writeheader()
            
        writer.writerows(dic)


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


def handle_rows(headers=None, rows=None):
    handled = []

    for row in rows:
        handled.append( dict(zip(headers, row)) )

    return handled


def main():
    html = get_html(MASTER_AGREEMENTS_ENDPOINT)
    rows = handle_html(html)
    data = handle_rows(headers=rows[0], rows=rows[1:])
    pdb.set_trace()
    return len(new_rows)


if __name__=='__main__':
    
    try:
        results = main()

    except Exception as e:        
        raise e















