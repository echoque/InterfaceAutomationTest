#! /usr/bin/env python
#coding=utf-8

import logging
import requests
from initialization.sysconfig import sys_cfg


class BaseAPI:

    def __init__(self):
        logging.info("init base api interface")
        self.cop_id=sys_cfg.get('corp_para','corp_id')
        self.token_url= sys_cfg.get('corp_para','token_url')
        self.res = ''

    def get_token(self,secret):

        params = {'corpid':self.cop_id,'corpsecret':secret}
        logging.info('params'+str(params))
        logging.info('token_url:'+self.token_url)
        token_res = requests.get(self.token_url,params=params)
        logging.info('responselog'+str(token_res.json()))
        return token_res.json().get('access_token')

    def post_json(self,url,json_obj,params=None):
        if params:
            self.res = requests.post(url,json=json_obj,params=params)
        else:
            self.res = requests.post(url, json=json_obj)

    def get_response(self):
        return self.res.json()

"""
上传图片
1、请求参数需传入access_token：调用test_get_access_token()
2、请求body需传入media_id ：调用test_get_media_id()
"""


##参考接口文档https://work.weixin.qq.com/api/doc#90000/90135/90236
def send_image(self):
    access_token=self.get_token(secret='')
    media_id=get_media_id()
    image_body_json={
   "touser" : "ZhongYaQi",
   # "toparty" : "PartyID1|PartyID2",
   # "totag" : "TagID1 | TagID2",
   "msgtype" : "image",
   "agentid" : 1000003,
   "image" : {
        "media_id" : media_id
   },
   "safe":0
}
    payload={
        'access_token':access_token
    }
    print(media_id,access_token)
    url='https://qyapi.weixin.qq.com/cgi-bin/message/send'
    res=requests.post(url,json=image_body_json,params=payload,proxies=myproxy)
    print(res.json())
    assert res.json().get('errmsg')=="ok"
    assert res.json().get('errcode')==0

##参考接口文档https://work.weixin.qq.com/api/doc#90000/90135/91039

##参考接口文档https://work.weixin.qq.com/api/doc#90000/90135/90253
def get_media_id(self):
    access_token=self.get_token(secret='')
    payload={
        'access_token':access_token,
        'type':'image'
    }
    url='https://qyapi.weixin.qq.com/cgi-bin/media/upload'
    ##http://docs.python-requests.org/en/master/user/quickstart/#post-a-multipart-encoded-file
    files={'media':('wz_20190330222654.jpg',open('C:\\Users\\zhongyaqi\\Desktop\\wz_20190330222654.jpg','rb'),'image/jpg')}
    res=requests.post(url,files=files,params=payload)
    return res.json().get('media_id')
    assert res.json().get('errmsg')=='ok'


