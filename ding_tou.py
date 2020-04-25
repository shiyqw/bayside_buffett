import csv
import requests
import datetime
from matplotlib import dates as mdates
from matplotlib import pyplot as plt

def get_data(code):
    r = requests.get('https://query1.finance.yahoo.com/v7/finance/download/%s?'
           'period1=100&period2=1587600000&interval=1d&events=history' % (code,))
    lines = r.text.split('\n')
    data[code], start_month = {}, lines[1][0:7]
    for line in lines[1:]:
        column = line.split(',')
        try:
            data[code][column[0][0:7]] = float(column[1])
        except ValueError:
            continue
    return start_month

def get_money(start_month, end_month):
    for code in data:
        money[code], current_eq = {}, 0.
        for month in sorted(data[code]):
            if month >= start_month and month <= end_month:
                money[code][month] = current_eq * data[code][month]
                current_eq += 10000. / data[code][month]

start_month, data, money = '1969-01', {}, {}
codes = raw_input('Input the codes: ')
for code in codes.split(','):
    start_month = max(start_month, get_data(code))

start_month = raw_input('Input the start month (after %s): ' % (start_month,))
end_month = raw_input('Input the end month (before 2020-04): ')
get_money(start_month, end_month)
    
ax = plt.gca()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
ax.xaxis.set_major_locator(mdates.YearLocator()) 
noop = []
for code in money:
    months = sorted(money[code])
    x_value = [datetime.datetime.strptime(m, '%Y-%m').date() for m in months]
    y_value = [money[code][m] for m in months]
    x_noop, y_noop = [x_value, range(0, len(x_value)*10000, 10000)]
    plt.plot(x_value, y_value, label=code)

plt.plot(x_noop, y_noop, label='NOOP')
plt.legend(loc='upper left')
plt.show()
