from ydata_profiling import ProfileReport
import pandas as pd
import os

input_file_path = 'data/car.data'
output_file_path = 'data/cardata.csv'
output_report_path = 'profiling/profiling.html'

column_headers = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'condition']

if not os.path.exists(os.path.dirname(output_report_path)):
    os.makedirs(os.path.dirname(output_report_path))

df = pd.read_csv(input_file_path, delimiter=',', header=None, names=column_headers)

df.to_csv(output_file_path, index=False)

df = pd.read_csv(output_file_path)

profile = ProfileReport(df, title="Profiling Report")
profile.to_file(output_report_path)
