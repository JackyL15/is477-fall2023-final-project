import requests
import hashlib
import zipfile
import os
import pandas as pd

url_car_zip = 'https://archive.ics.uci.edu/static/public/19/car+evaluation.zip'

response = requests.get(url_car_zip)
if response.status_code == 200:
    with open('car+evaluation.zip', mode='wb') as f:
        f.write(response.content)

    with open('car+evaluation.zip', mode='rb') as f:
        data = f.read()
        sha256hash = hashlib.sha256(data).hexdigest()

    if sha256hash == expected_hash_adult:
        print("1559d51dcf327f4f8c71b711ceed7fd95a382fc8d8e1998667f4f23b82860403")

        if not os.path.exists('data'):
            os.makedirs('data')

        with zipfile.ZipFile('car+evaluation.zip', 'r') as zip_ref:
            zip_ref.extractall('data')

        file_path = 'data/car.data'
        df = pd.read_csv(file_path, delimiter=',', header=None)
        output_path = 'data/cardata.csv'
        column_headers = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'condition']
        df.columns = column_headers
        df.to_csv(output_path, index=False)

    else:
        print("Computed hash does not match expected hash for car dataset")
else:
    print(f"Could not download car evaluation.zip. Status code: {response.status_code}")
