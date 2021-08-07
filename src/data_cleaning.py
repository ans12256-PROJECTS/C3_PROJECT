# August 6, 2021
# data processing pieces

import numpy as np
import pandas as pd


def read_clean_places():
    '''
    Returns read_places_indexed dataframe

    Read clean places data
    "clean" means the following
    1) gps data is split from a list to two columns
    2) gps data is further cleaned for "out in space" gps by scaling by 1/1e6 ~ 2.46% of data
    3) no gps data records are dropped - too labor intensive to collect gps from addresses
    4) Mulitple gPlusPlaceId manipulations as follows
        4.1) gPlusPlaceId are rounded by round(gPlusPlaceId/1e11) to nearest integer
             for example Eiffel Tower did not match gPlusPlaceId otherwise (21 digits)
        4.2) Duplicate gPlusPlaceId's are dropped 0.83% of data

    gPlusPlaceId_index is intended to be used on reviews data after gps box subselection
    '''
    % % time
    read_places_indexed = pd.read_json('data/places_gps_no_dup_indexed.json')
    read_places_indexed.set_index('gPlusPlaceId_index', inplace=True)
    # beepy.beep(sound=4)  # 4 : 'ping' # optional if beepy is installed
    # read_places_indexed.head()

    return read_places_indexed


if __name__ == '__main__':
    # return dataframe
    places_indexed = read_clean_places()
