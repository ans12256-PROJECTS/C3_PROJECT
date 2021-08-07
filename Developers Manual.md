# Developers Manual

# Raw Data
data/reviews_gps_box.json # 50 miles box @ zip 98012
data/places_gps_box.json #  50 miles box @ zip 98012

* delme.json
gPlusPlaceId_filter.json
places.clean.json
places.json
places_gps.json
* places_gps_no_dup_indexed.json
  gPlusPlaceId_index, no duplicates, gps two columns
* reviews_gPlusPlaceId_index_no_duplicates.json
  ready for gps box filter
* places_revs_count.json
places_sub.json
places_sub_gps.json
reviews.clean.json
reviews.json
reviews_sub.json
*users.clean.json
users.json
*users_sub.json

# Data Processing
## pd.read_json() does not work

## Data Cleaning
[data_cleaning.py](src/data_cleaning.py)
    def read_clean_places() - read clean indexed places file
        refer docstring for more details


# Data subsampling

# Data Structure
