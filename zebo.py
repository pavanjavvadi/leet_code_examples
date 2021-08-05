from urllib.parse import urlencode

Smac = 562949953422759
netnum = 27017

vars = {'smac': Smac, 'netnum': netnum, 'rg':'true', 'epoch':1620297000, 'diff':10800}

base_url = "https://www.lizardmonitoring.com/app/sensor/showDetail?"

print(base_url +urlencode(vars))



