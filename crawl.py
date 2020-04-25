import requests
code = raw_input("Input the code: ")
print code
link = 'https://query1.finance.yahoo.com/v7/finance/download/%s?period1=1000&period2=1587600000&interval=1d&events=history' % (code,)
r = requests.get(link)
r.status_code
r.headers['content-type']
r.encoding
t = r.text
print t
