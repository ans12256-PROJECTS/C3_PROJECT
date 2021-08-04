# August 2, 2021; Alexey Smirnov
# json "converter" of google data "clean.json" files
# refer https://cseweb.ucsd.edu/~jmcauley/datasets.html#google_local
# places.clean.json, reviews.clean.json, user.clean.json
# all "clean" files are essentially rows of dictionaries, that can not
#  be imported(could not figure it out directly) usign standard pd.read_json()
# resulting in errors
# the following is a compilation of multiple sources to "convert" "clean"
# data files to a json files directly readable by
# df=pd.read+json('dat_file.json')

import time  # for execution time reference

import numpy as np
import pandas as pd

#  =============== places.clean.json

start_total = time.time()

# STEP 1 df_places
# read whole file into a single column dataframe
# with each row (single column) as a string'ed dictionary:
# "{'name': u'Diamond Valley Lake Marina', 'price': None, 'address': [u'2615 Angler Ave' ...}"
start = time.time()
df_places = pd.DataFrame(open('../data/places.clean.json'))
print(f'STEP 1 df_places load time: {time.time() - start}')

# STEP 2 df_places
# explode single column of dictionaries into proper columns
start = time.time()
df_places = df_places[0].apply(lambda x: pd.Series(eval(x)))
print(f'STEP 2 df_places explode time: {time.time() - start}')


# STEP 3 df_places
# save as clead direct read json
start = time.time()
df_places.to_json('../data/places.json')
print(f'STEP 3 df_places save json time: {time.time() - start}')

# STEP 4 clear df_places from memory, and reload in a single step
# save as clead direct read json
start = time.time()
del df_places
df_places=pd.read_json('../data/places.json')
print(f'STEP 4 df_places reload from json time: {time.time() - start}')
del df_places

#  =============== reviews.clean.json

# STEP 1 df_reviews
# read whole file into a single column dataframe
# with each row (single column) as a string'ed dictionary:
# "{'name': u'Diamond Valley Lake Marina', 'price': None, 'address': [u'2615 Angler Ave' ...}"
start = time.time()
df_reviews = pd.DataFrame(open('../data/reviews.clean.json'))
print(f'STEP 1 df_reviews load time: {time.time() - start}')

# STEP 2 df_reviews
# explode single column of dictionaries into proper columns
start = time.time()
df_reviews = df_reviews[0].apply(lambda x: pd.Series(eval(x)))
print(f'STEP 2 df_pdf_reviews explode time: {time.time() - start}')


# STEP 3 df_reviews
# save as clead direct read json
start = time.time()
df_reviews.to_json('../data/reviews.json')
print(f'STEP 3 df_reviews save json time: {time.time() - start}')

# STEP 4 clear df_reviews from memory, and reload in a single step
# save as clead direct read json
start = time.time()
del df_reviews
df_reviews=pd.read_json('../data/reviews.json')
print(f'STEP 4 df_reviews reload from json time: {time.time() - start}')
del df_reviews


#  =============== users.clean.json

# STEP 1 df_users
# read whole file into a single column dataframe
# with each row (single column) as a string'ed dictionary:
# "{'name': u'Diamond Valley Lake Marina', 'price': None, 'address': [u'2615 Angler Ave' ...}"
start = time.time()
df_users = pd.DataFrame(open('../data/users.clean.json'))
print(f'STEP 1 df_users load time: {time.time() - start}')

# STEP 2 df_users
# explode single column of dictionaries into proper columns
start = time.time()
df_users = df_users[0].apply(lambda x: pd.Series(eval(x)))
print(f'STEP 2 df_users explode time: {time.time() - start}')


# STEP 3 df_users
# save as clead direct read json
start = time.time()
df_users.to_json('../data/users.json')
print(f'STEP 3 df_users save json time: {time.time() - start}')

# STEP 4 clear df_users from memory, and reload in a single step
# save as clead direct read json
start = time.time()
del df_users
df_users=pd.read_json('../data/users.json')
print(f'STEP 4 df_users reload from json time: {time.time() - start}')
del df_users


print(f'Total run time: {round((time.time() - start_total)/60, 2)} minutes')
