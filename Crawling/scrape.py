import requests
from bs4 import BeautifulSoup
import numpy as np
import random
import time
import pandas as pd
import os
import concurrent.futures

directory = '.'
links = pd.read_csv('./AllLinks.csv')
links['Index'] = links.index
links = links.sort_index()
links = links.iloc[90:100,:]

def record_mobile_features(url):

    url_idx = url['Index']
    url = url['Link']

    headers = {'User-Agent': 'Chrome/120.0.0.0', 'Accept-Language': 'en-US'}
    time.sleep(random.randint(10, 12))

    page = requests.get(url, headers=headers, timeout=5)
    soup = BeautifulSoup(page.content, 'html.parser')

    details = soup.find_all(id = 'specs-list')
    parts = details[0].find_all('table')


    sections_set = {}
    num_section = len(parts)

    product_name = soup.find_all('title')[0].text.strip()
    sections_set['Name'] = {'Name':[product_name]}

    for sec_idx in range(num_section):
        section_name = parts[sec_idx].find_all('th')[0].text.strip()

        sub_section = parts[sec_idx].find_all('tr')

        num_sub_section = len(sub_section)
        sub_sections_set = {}
        for sub_sec_idx in range(num_sub_section):
            try:
                name_sub_section = sub_section[sub_sec_idx].find_all('td')[0].text.strip()

                if len(name_sub_section) == 0:
                    name_sub_section = f'{section_name}_Extra'
                else:
                    name_sub_section = f'{section_name}_{name_sub_section}'
                # sub_sections_set[name_sub_section] = [_.strip() for _ in sub_section[sub_sec_idx].find_all('td')[1].text.strip().split('\n')]
                sub_sections_set[name_sub_section] = sub_section[sub_sec_idx].find_all('td')[1].text.strip()
            except IndexError:
                continue
        
        sections_set[section_name] = sub_sections_set
    
    record = {}
    for d in sections_set.values():
        record.update(d)

    record['Index'] = url_idx
    print(f'Index {url_idx} recoreded.')
    
    return record

def scrape_all_links(urls):

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:

        futures = [executor.submit(record_mobile_features, urls.loc[urls['Index']==idx, :]) for idx in urls.index]

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            results.append(pd.DataFrame(result))
            
    result_df = pd.concat(results)
    
    return result_df

df = scrape_all_links(links)

pd.merge(df, links, on='Index').to_csv('Scrape_Dataset.csv', index=False)