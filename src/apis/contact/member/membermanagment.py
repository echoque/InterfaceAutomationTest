#! /usr/bin/env python
#coding=utf-8
import logging
import pytest,codecs,json
from apis.baseapi import BaseAPI
from initialization.sysconfig import sys_cfg

class MemberManagment(BaseAPI):

    def __init__(self):
        BaseAPI.__init__(self)
        logging.info("Init department management API")
        self.dep_secure = sys_cfg.get('contact_para','secure')
        self.create_mem_url = sys_cfg.get('contact_para','create_mem_url')

    def get_new_member(self,file_name):

        with codecs.open(file_name,'r',encoding='utf8') as f:
            json_object=json.loads(f.read(),encoding='utf8')
            logging.debug('json_object'+str(json_object))
            return json_object

    def create_member(self,file_name):
        new_member=self.get_new_member()
        param = {'access_token':self.get_token(self.dep_secure)}
        logging.debug("url:"+str(self.create_dep_url))
        logging.debug("params:" + str(param))
        self.post_json(self.create_mem_url,new_member,params=param)

    @pytest.mark.parametrize("name", [
            ('echo_test'),(20,"yaqi_test")])
    def create_dept_by_params(self,name):
        new_part={
       "name": name,
       "parentid": 1,
       "order": 1
        }

        param = {'access_token':self.get_token(self.dep_secure)}
        logging.debug("url:"+str(self.create_dep_url))
        logging.debug("params:" + str(param))
        self.post_json(self.create_dep_url,new_part,params=param)

    def update_department(self):

        update_part={
       "id": 2,
       "name": "yaqi20190331",
       "parentid": 1,
       "order": 1
}
        param = {'access_token':self.get_token(self.dep_secure)}
        self.post_json(self.update_dep_url,update_part,params=param)

    def get_create_dept_res(self):
        return self.get_response()
