import requests
from bs4 import BeautifulSoup
import numpy as np
import random
import time
import pandas as pd
import os

directory = '.'
links = pd.read_csv('C:/Users/ztava/Downloads/Zahra_AllLinks.csv')

def record_mobile_features(url):

    headers = {'User-Agent': 'Chrome/120.0.0.0', 'Accept-Language': 'en-US'}
    time.sleep(random.randint(8, 10))

    page = requests.get(url, headers=headers, timeout=5)
    soup = BeautifulSoup(page.content, 'html.parser')

    details = soup.find_all(id = 'specs-list')
    parts = details[0].find_all('table')


    sections_set = {}
    num_section = len(parts)

    product_name = soup.find_all('title')[0].text.split('-')[0].strip()
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

    return record

def make_dataset(links, file_path):

    loop_threshold = 10
    num_loop = 1

    first_idx = links.index.tolist()[0]
    last_idx = links.index.tolist()[-1]

    records = pd.DataFrame()

    for idx in range(first_idx, last_idx+1):
        url = links['Link'][idx]

        while num_loop < loop_threshold:
            try:
                mobile_info = record_mobile_features(url)
                records = pd.concat([records, pd.DataFrame(mobile_info)])
                print(f'url index {idx} recorded.')
                num_loop = 1
                break

            except Exception as e:
                print(e)
                num_loop += 1
                records.sort_index(axis = 1).to_csv(file_path, index=False)
                continue
    
    records.sort_index(axis = 1).to_csv(file_path, index=False)
    return records

make_dataset(links,os.path.join(directory,'mobile_scrap.csv'))
