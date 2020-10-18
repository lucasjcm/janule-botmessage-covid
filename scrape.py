import urllib.request

try:
    # Source: https://covidtracking.com/data/national
    # Headers: date,death,deathIncrease,inIcuCumulative,inIcuCurrently,hospitalizedIncrease,hospitalizedCurrently,hospitalizedCumulative,negative,negativeIncrease,onVentilatorCumulative,onVentilatorCurrently,posNeg,positive,positiveIncrease,recovered,states,totalTestResults,totalTestResultsIncrease
    covid_data = urllib.request.urlopen('https://covidtracking.com/data/download/national-history.csv').readlines()
except Exception as e:
    for key, value in e.__dict__.items():
        print('------------------------------- EXCEPTION CAUGHT -------------------------------')
        print(key, value)
        print('--------------------------------------------------------------------------------')

# headers = covid_data[0]
latest_day_data = covid_data[1].decode('utf-8').split(',')

datestring = latest_day_data[0].strip('"')
total_deaths = int(latest_day_data[1])
new_deaths = int(latest_day_data[2])

# TODO: Add USA flag emoji.
print(f'Total deaths (USA) as of {datestring}: {total_deaths:,} ({new_deaths:,} new)')