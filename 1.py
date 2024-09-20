import requests
from lxml import etree
from fake_useragent import UserAgent

url = 'https://www.baidu.com/'
header = {
    'User-Agent':UserAgent().chrome
}
resp = requests.get(url,headers=header)
e = etree.HTML(resp.text)
msgs = e.xpath('//title/text()')
print(msgs)
