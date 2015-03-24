# -*- coding: utf-8 -*-


from model.contact import Contact
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_new_contact(app):
    success = True
    app.open_home_page()
    app.login(username="admin",password= "secret")
    app.fill_form(Contact(first_n= "first",mid_n= "middle",last_n= "last",nick_n= "kuk",company= "adda",address= "575 oiweojdckjgsd,russia",home_ph= "12134519827",
                cell_ph= "120092340980",email= "first.lastmiddle.@adda.com"))
    app.fill_drop_down_boxes()
    app.fill_end_form()
    app.logout()



