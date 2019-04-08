#! usr/bin/env python

from src.apis.contact.member.membermanagment import MemberManagment


class Testcreatemem:
    def test_createmem(self):
        member=MemberManagment()
        member.create_member_by_file()
        response=member.get_create_mem_res()
        assert response.get("errmsg")=='created'
