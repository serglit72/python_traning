# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalazer(fixture.destroy)
    return fixture

def test_test_add_group(app):
    app.session.login(username= "admin",password="secret")
    app.create_fill_group_form(Group( name="Groupe4",header="Groun",footer="groupe"))
    app.session.logout()

def test_test_empty_group(app):
    app.session.login(username= "admin",password= "secret")
    app.create_fill_group_form(Group(name="",header= "",footer= ""))
    app.session.logout()
