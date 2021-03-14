import requests
import json
import time
data={'account':'13560661721',
      'app_id':'cn.vanber.xixunyun.saas',
      'app_version':'4.1.5',
      'key':'',
      'model':'SM-G955N',
      'password':'loveZZZ.',
      'platform':'2',
      'registration_id':'160a3797c8437218079',
      'request_source':'3',
      'school_id':'177',
      'system':'4.4.2',
      'uuid':'48:45:20:B9:D7:19'}
login_header={
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '227',
        'Host': 'api.xixunyun.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.8.1',

}
login_url=' https://api.xixunyun.com/login/api?from=app&version=4.1.5&platform=android&entrance_year=0&graduate_year=0'
request=requests.post(url=login_url,headers=login_header,data=data)
login_data=json.loads(request.text)
token=login_data['data']['token']
time.sleep(1)

latitude='113.387809'
longitude='22.419439'
print(login_data)
sign_url='https://api.xixunyun.com/signin?token='+token+'&from=app&version=4.1.5&platform=android&entrance_year=0&graduate_year=0 '
sign_data={'address':'中山市中等专业学校',
           'address_name':'广东省中山市五桂山石鼓中山职业教育园区中山中专学校',
           'change_sign_resource':'0',
           'comment':'',
           'latitude':latitude, 
           'longitude':longitude,
           'remark':'0',
              
    } 
sign_request=requests.post(url=sign_url,data=sign_data,headers=login_header)
sign=json.loads(sign_request.text) 
print(sign)
