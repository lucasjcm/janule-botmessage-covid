import urllib.request

try:
    # Source: https://github.com/nytimes/covid-19-data
    # Columns (only first 3 are used): date,cases,deaths,confirmed_cases,confirmed_deaths,probable_cases,probable_deaths
    covid_data = urllib.request.urlopen(
        'https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us.csv').readlines()
except Exception as e:
    for key, value in e.__dict__.items():
        print('------------------------------- EXCEPTION CAUGHT -------------------------------')
        print(key, value)
        print('--------------------------------------------------------------------------------')

# headers = covid_data[0]
latest_day_data = covid_data[1].decode('utf-8').split(',')

datestring = latest_day_data[0]
total_cases = int(latest_day_data[1])
total_deaths = int(latest_day_data[2])

def generate_flag_emoji(country_code):
    """
    :param str country_code: A two letter all-caps country code like "US". it's actually called a regional indicator
                             symbol. See here: https://en.wikipedia.org/wiki/Regional_indicator_symbol

    Also see:
     - (main source) https://schinckel.net/2015/10/29/unicode-flags-in-python/
     - (linked above in main source) https://esham.io/2014/06/unicode-flags

    :rtype str: Generated flag emoji
    """
    OFFSET = ord('🇦') - ord('A') 
    return chr(ord(country_code[0]) + OFFSET) + chr(ord(country_code[1]) + OFFSET)

us_flag_emoji = generate_flag_emoji('US')

stats_str = f'{us_flag_emoji} {datestring}: {total_cases:,} total cases, {total_deaths:,} total deaths'
source_str = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us.csv'

print(f'{stats_str} | {source_str}')
