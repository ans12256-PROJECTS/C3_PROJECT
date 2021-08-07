# August 3, 2021
# subsample original data to reduce modeling time
# run from directory above src
#  since paths are relative and are hard coded
#
# python src/sub_sample_data.py

import pandas as pd
import numpy as np
import random
import time  # for execution time reference
start_total = time.time()


# Can be made a parameter, or three different parameters
n_samples = 10000

original_data_files = ['users.json', 'places.json', 'reviews.json']

for data_file_name in original_data_files:
    # =========  SMALLEST database
    # users.json 764.2 Mb
    # places.json 1.07 Gb
    # reviews.json 4.57 Gb
    # Wall time: 46.9 s, 7.9 GB, or + 7.7 Gb from .764 Gb * 10 ?
    start = time.time()
    print(f'STEP 1 loading data/{data_file_name}')
    df = pd.read_json('data/'+data_file_name)
    print(f'STEP 1 data/{data_file_name} load time: \
        {round((time.time() - start_total)/60, 2)} minutes')
    # df.shape # (3,747,937, 6)
    # df.columns ['userName', 'jobs', 'currentPlace', 'previousPlaces', 'education', 'gPlusUserId']

    # help(df.sample)
    start = time.time()
    print(f'STEP 2 subsampling and saving {data_file_name}_sub.json')
    df_sub = df.sample(n=10000, random_state=1)  # frac=0.1
    # # df_users_sub.head()
    # # df_users_sub.shape # (10000, 6)
    sub_file_name = data_file_name.split('.json')[0] + '_sub.json'
    df_sub.to_json('data/'+sub_file_name)
    del df, df_sub
    print(f'STEP 2 {sub_file_name} save time: \
        {round((time.time() - start_total)/60, 2)} minutes')
    # %%time
    start = time.time()
    print(f'STEP 3 reading {sub_file_name}')
    df_sub = pd.read_json('data/'+sub_file_name)  # Wall time: 263 ms
    # df_users_sub.head()
    del df_sub
    print(f'STEP 3 {sub_file_name} save time: \
        {round((time.time() - start_total)/60, 2)} minutes')


print(f'Total run time: {round((time.time() - start_total)/60, 2)} minutes')

#  Output reference
# (tf2) alexey_imac@ALEXEYs-iMac C3_PROJECT % python src/sub_sample_data.py
# STEP 1 loading data/users.json
# STEP 1 data/users.json load time:         0.72 minutes
# STEP 2 subsampling and saving users.json_sub.json
# STEP 2 users_sub.json save time:         0.79 minutes
# STEP 3 reading users_sub.json
# STEP 3 users_sub.json save time:         0.79 minutes
# STEP 1 loading data/places.json
# STEP 1 data/places.json load time:         1.57 minutes
# STEP 2 subsampling and saving places.json_sub.json
# STEP 2 places_sub.json save time:         1.66 minutes
# STEP 3 reading places_sub.json
# STEP 3 places_sub.json save time:         1.66 minutes
# STEP 1 loading data/reviews.json
# STEP 1 data/reviews.json load time:         3.81 minutes
# STEP 2 subsampling and saving reviews.json_sub.json
# STEP 2 reviews_sub.json save time:         3.92 minutes
# STEP 3 reading reviews_sub.json
# STEP 3 reviews_sub.json save time:         3.92 minutes
# Total run time: 3.92 minutes
