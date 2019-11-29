import requests


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
headers = {'User-Agent': user_agent}

session = requests.session()
r = session.get('https://mail.gialen.com:8443/coremail/')
print(r.status_code)

data = {
    "locale": "zh_CN",
    "nodetect": "false",
    "destURL": "",
    "supportLoginDevice": "true",
    "accessToken": "",
    "timestamp": "",
    "signature": "",
    "nonce": "",
    "device": "{\"uuid\":\"webmail_windows\",\"imie\":\"webmail_windows\",\"friendlyName\":\"firefox+70\",\"model\":\"windows\",\"os\":\"windows\",\"osLanguage\":\"zh-CN\",\"deviceType\":\"Webmail\"}",
    "supportDynamicPwd": "true",
    "supportBind2FA": "true",
    "authorizeDevice": "",
    "loginType": "",
    "uid": "lingfangyuan@gialen.com",
    "password": "Lfy19931",
    "face": "auto",
    "faceName": "自动选择",
    "action:login": ""
}

r = session.post('https://mail.gialen.com:8443/coremail/index.jsp?cus=1',
        data=data, headers=headers)
print(r.status_code)
print(dict(r.cookies))
print(r.text)