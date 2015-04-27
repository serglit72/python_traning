__author__ = 'Sergei'

from model.contact import Contact

def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create_c(Contact(first_n= "first",mid_n= "middle",last_n= "last",nick_n= "kuk",company= "adda",address= "575 oiweojdckjgsd,russia",home_ph= "12134519827",
        cell_ph= "120092340980",email= "first.lastmiddle.@adda.com"))
    old_contact = app.contact.get_contact_list()
    app.contact.contact_delete()
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
    old_contact[0:1] = []
    assert old_contact == new_contact
