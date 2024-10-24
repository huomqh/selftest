import requests
con=requests.get('www.baidu.com')
print(con.text)
