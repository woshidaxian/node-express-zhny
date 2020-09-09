import urllib
import urllib2
import sys
import ssl


host = 'https://weather01.market.alicloudapi.com'
path = '/spot-to-weather'
method = 'GET'
appcode = '22f301375c004340bdb0e6e7da6db7e3'
querys = 'area=%E6%B3%B0%E5%B1%B1&need3HourForcast=0&needAlarm=0&needHourData=0&needIndex=0&needMoreDay=0'
bodys = {}
url = host + path + '?' + querys

request = urllib2.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib2.urlopen(request, context=ctx)
content = response.read()
if (content):
    print(content)
