#! /usr/bin/env python
#coding=utf-8

from apis.contact.department.depmanagment import DeptManagment

class TestCreateDep:

    def test_create_new_dep(self):
        dept_managment = DeptManagment()
        dept_managment.create_dept()
        create_res = dept_managment.get_response()
        assert create_res.get('errmsg')=='created'

    # def test_create_new_dep_by_params(self):
    #     dept_managment = DeptManagment()
    #     dept_managment.create_dept()
    #     create_res = dept_managment.get_response()
    #     assert create_res.get('errmsg')=='created'

