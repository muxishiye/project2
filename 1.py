import requests
from lxml import etree

resp = requests.get('https://www.baidu.com')
e = etree.HTML(resp)
msg = e.xpath('//h1')
print(msg)