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

        with codecs.open(file_name,'r',encoding='utf-8') as f:
            json_object=json.loads(f.read(),encoding='utf-8')
            print('*******type'+type(json_object))
            logging.debug('json_object'+str(json_object))
            return json_object
        logging("json_object**:"+json_object)

    def get_new_member_test(self,file_name):
        # file_name=r"E:\光荣之路\测试开发\corweixindemo\corweixindemo\testdata\member.json.py"
        with open(file_name,encoding='utf-8') as f:
            # logging("******f"+str(f))
            # logging("typef"+type(f))
            json_object = json.load(f,encoding='utf-8')
            # logging('*******type'+type(json_object))
            return json_object
            # return str(json_object)
        logging(str(json_object))

    # def get_new_member_test(self,file_name, JSONDecodeError=None):
    #     try:
    #         obj, end = self.scan_once(file_name, 0)
    #     except StopIteration as err:
    #         raise JSONDecodeError("Expecting value", file_name, err.value) from None
    #     return obj, end


    def create_member(self):
        # file_name=r"E:\光荣之路\测试开发\corweixindemo\corweixindemo\testdata\member.json.py"
        # new_member=self.get_new_member_test(file_name)
        new_member_test= {
    "userid": "yaqi",
    "name": "仲雅琦",
    "alias": "jackzhang",
    "mobile": "153215421223",
    "department": [1, 2],
    "order":[10,40],
    "position": "产品经理",
    "gender": "1",
    "email": "zhongyaqi@gzdev.com",
    "is_leader_in_dept": [1, 0],
    "enable":1,
    # "avatar_mediaid": "2-G6nrLmr5EC3MNb_-zL1dDdzkd0p7cNliYu9V5w7o8K0",
    "telephone": "550-123456",
    "address": "广州市海珠区新港中路"}

        param = {'access_token':self.get_token(self.dep_secure)}
        logging.debug("url:"+str(self.create_mem_url))
        logging.debug("params:" + str(param))
        self.post_json(self.create_mem_url,new_member_test,params=param)

    def create_member_by_file(self):
        file_name=r"E:\光荣之路\测试开发\corweixindemo\corweixindemo\testdata\member.json.py"
        new_member=self.get_new_member_test(file_name)
        param = {'access_token':self.get_token(self.dep_secure)}
        logging.debug("url:"+str(self.create_mem_url))
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

    def update_member(self):

        update_part={
       "id": 2,
       "name": "yaqi20190331",
       "parentid": 1,
       "order": 1
}
        param = {'access_token':self.get_token(self.dep_secure)}
        self.post_json(self.update_dep_url,update_part,params=param)

    def get_create_mem_res(self):
        return self.get_response()

# if __name__ == '__main__':
#     test = MemberManagment()
#     file_name=r"E:\光荣之路\测试开发\corweixindemo\corweixindemo\testdata\member.json.py"
#
#     aa=test.get_new_member_test()
#     print(aa)