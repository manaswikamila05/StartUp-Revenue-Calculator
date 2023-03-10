import datetime

# less categorical data, so just used dictionaries.

TYPE_DICT = {'IL' : 1, 'FC' : 2, 'DT' : 3}

CITY_DICT = {'Izmir': 1, '': 2, 'Mugla': 3,
'Tekirdag': 4, 'Kutahya': 5, 'Afyonkarahisar': 6,
'Adana': 7, 'Kirklareli': 8, 'Elazig': 9,
'Aydin': 10, 'Gaziantep': 11, 'Ankara': 12, 'Kayseri': 13,
'Sakarya': 33, 'Tokat': 15, 'Eskisehir': 17, 'Bolu': 18,
'Sanliurfa': 19, 'Trabzon': 20, 'Kocaeli': 21, 'Samsun': 22,
'Usak': 23, 'Kastamonu': 24, 'Antalya': 34, 'Karabuk': 25,
'Isparta': 26, 'Denizli': 27, 'Diyarbakir': 35, 'Osmaniye': 29,
'Amasya': 30, 'Balikesir': 31, 'Bursa': 32, 'Edirne': 14,
'Istanbul': 16, 'Konya': 28}

GROUP_DICT = {'Big Cities' : 1, 'Other' : 2}



def city_conv(x):
    if x in CITY_DICT:
        return CITY_DICT[x]
    else:
        return 0

def type_conv(x):
    if x in TYPE_DICT:
        return TYPE_DICT[x]
    else:
        return 0

def group_conv(x):
    if x in GROUP_DICT:
        return GROUP_DICT[x]
    else:
        return 0

def f(x):
    try:
        val = float(x)
        return val
    except:
        return 0

def date_processing(pd_date):
    t = datetime.datetime(pd_date.year, pd_date.month, pd_date.day, 0, 0, 0)
    return (t-datetime.datetime(1970,1,1)).total_seconds()