import requests
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
url='https://passport.weibo.cn/sso/login'
data={'username':'13272729885','password':'123456','savestate':'1','r':'','ec':'0','pagerefer':'',\
'entry':'mweibo',\
'wentry':'',\
'loginfrom':'',\
'client_id':'',\
'code':'',\
'qq':'',\
'mainpageflag':'1',\
'hff':'',\
'hfp':''}

header={'Accept':'*/*',\
'Accept-Encoding':'gzip, deflate, br',\
'Accept-Language':'zh-CN,zh;q=0.8',\
'Connection':'keep-alive',\
'Content-Length':'145',\
'Content-Type':'application/x-www-form-urlencoded',\
# 'Cookie':'_T_WM=e7147f3bae52a1c7f341a3ae9b423f6f; WEIBOCN_FROM=1110005030; MLOGIN=0; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D1076032293572412%26uicode%3D10000011%26fid%3D102803; login=903b2dfe558d757c50a86dbd7d018964'
'Host':'passport.weibo.cn',\
'Origin':'https://passport.weibo.cn',\
'Referer':'https://passport.weibo.cn/signin/login',\
'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Mobile Safari/537.36'
}
session=requests.Session()
session.post(url,data,header)
html=session.get('https://m.weibo.cn/')
html.encoding='utf-8'
print(html.text.encode('utf-8').decode('unicode-escape'))