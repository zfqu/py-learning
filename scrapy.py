import urllib2,pandas

url = 'http://ichart.finance.yahoo.com/table.csv?s=GE&d=10&e=5&f=2013&g=d&a=0&b=2&c=1962&ignore=.csv'

ge_csv = urllib2.urlopen(url)



ge = pandas.read_csv(ge_csv, index_col=0, parse_dates=True)
ge.plot(y='Adj Close')