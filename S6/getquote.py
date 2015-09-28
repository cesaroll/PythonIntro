import urllib, re, sys

symbol = sys.argv[1]

#url = 'http://finance.google.com/finance?q='
url = 'http://localhost/test.html'

#content = urllib.urlopen(url + symbol).read()
content = urllib.urlopen(url).read()

m = re.search('span id="ref.*>(.*)<', content)

if m:
    quote = m.group(1)
else:
    quote = 'no quote for symbol: ' + symbol
    
print(quote)

