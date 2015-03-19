# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@ pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalazer(fixture.destroy)
    return fixture

    def test_test_add_group(app):
        app.Login(username= "admin",password="secret")
        app.create_fill_group_form(Group( name="Groupe4",header="Groun",footer="groupe"))
        app.logout()

    def test_test_empty_group(app):
        app.Login(username= "admin",password= "secret")
        app.create_fill_group_form(Group(name="",header= "",footer= ""))
        app.logout()


