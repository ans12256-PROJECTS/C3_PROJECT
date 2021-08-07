# https://en.wikipedia.org/wiki/Earth_radius
# R_avg = 3,959 miles (3950~3963)
# GPS local search subsample
# given local coordinates, and radius, subsample df_places
import math
# Alexey's local USPS GPS from google maps
local = [47.85408756055844, -122.21958066838837]
# [latitude North-South, longitude East-West]; opposite order x(EW), y(NS) for geopandas
radius = 5  # miles


def check_gps(gps_list, radius):
    '''
    gps_list = [NS_gps, EW_gps] in decimal degrees (Google map right-click output)
    exampe: [47.85408756055844, -122.21958066838837] - 98012 USPS
    radius - desired radius of interest im miles

    https://en.wikipedia.org/wiki/Earth_radius
    R_avg = 3,959 miles (3950~3963)

    gps column in places.gps is in the form ['NS_latitudes','EW_longitudes']
    Valid gps coordinates are NS +- 90.0, EW +- 180.0
    There are incorrect NS 75755 (2.45%), EW 75369 (2.44%) of all data
    let's do square first
    IGNORE (BUG) flip through poles EW at exactly +-90.0, and +- at exactly 180.0
    R_avg = 3959 miles, 1/4 equator-> pole 2*PI*R/4 = 90.0, or
    PI*R/(180) = 1.0 in NS in miles

    Y_miles_NS_one_WAY_in_GPS_degrees = Y * 180/(PI * R_earth)

    R_ew = R_earth * cos(PI/180*NS_gps); R_earth at NS_gps = 0, 0 at NS_gps = +- 90.0

    X_miles_EW_one_WAY_in_GPS_degrees = X * 180/(PI * R_ew)

    import math
    math.pi
    3.141592653589793

    '''
    PI = math.pi  # 3.141592653589793
    R_earth = 3959  # Average Earth radius
    # Not GPS dependent going NS
    Y_miles_NS_one_WAY_in_GPS_degrees = radius * 180/(PI * R_earth)
    # GPS dependent on NS_gps - smaller EW circle
    R_ew = R_earth * math.cos(PI/180*gps_list[0])
    X_miles_EW_one_WAY_in_GPS_degrees = radius * 180/(PI * R_ew)

    return Y_miles_NS_one_WAY_in_GPS_degrees, X_miles_EW_one_WAY_in_GPS_degrees


def gps_box():
    '''
    Create a filter for given gps box
    '''

    # construct a filter based on given GPS +- box
    # AND notation as & https://pythoninoffice.com/filter-a-pandas-dataframe-or-and-not/
    gps_box = ((df.Y_NS_latitudes < curr_gps[0] + Y_NS_deg) & (df.Y_NS_latitudes > curr_gps[0] - Y_NS_deg)) & \
        ((df.X_EW_longitudes < curr_gps[1] + X_EW_deg) &
         (df.X_EW_longitudes > curr_gps[1] - X_EW_deg))
