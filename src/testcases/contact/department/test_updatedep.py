#! /usr/bin/env python
#coding=utf-8

from apis.contact.department.depmanagment import DeptManagment

class TestCreateDep:

    def test_update_dep(self):
        dept_managment = DeptManagment()
        dept_managment.update_department()
        create_res = dept_managment.get_response()
        assert create_res.get('errmsg')=='updated'
