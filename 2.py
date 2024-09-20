import requests
from fake_useragent import UserAgent
from lxml import etree

url = "https://www.faloo.com/"
header = {"User-Agent": UserAgent().edge}

resp = requests.get(url, headers=header)
resp.encoding = "gbk"

# 创建etree对象
e = etree.HTML(resp.text)
fic_name = e.xpath("//div[@class='bangBox']/ul/li/a/@title")
fic_url = e.xpath("//div[@class='bangBox']/ul/li/a/@href")

# 创建一个空字典，方便后面做去重
fiction = {}

for name, url in zip(fic_name, fic_url):
    # 对应书名和url地址并去重
    fiction[name] = url
print(fiction)