import pandas as pd
import re
import file_load as fl

def parse2df(path, names):
    rx_dict = {'data_regex' : re.compile(r'\d*\.?\d*\s\-?\d*.\d*\s\d*.\d*\s\-?\d*.\d*\n')}

    dfs = []
    for name in names:
        raw_dataset = fl.file_load(path, name)
        dataset = []
        for raw_data in raw_dataset:
            temp = re.match(rx_dict['data_regex'], raw_data)
            if temp:
                data = temp.group(0).strip('\n').split('\t')
                dataset.append([float(ind_data) for ind_data in data])
        df = pd.DataFrame(dataset, columns = ['wavelength (nm)', 'CD (mdeg)', 'HT (V)', 'OD'])
        dfs.append(df)
    return dfs
#this is a test change
#test for dev 
