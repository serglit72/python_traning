__author__ = 'Sergei'
from model.contact import Contact


def test_contact_new(app):
    old_contact = app.contact.get_contact_list()
    contacts = Contact(first_n="first", mid_n="middle",last_n="last",nick_n= "kuk",company= "adda",address= "575 oiweojdckjgsd,russia",home_ph= "12134519827",cell_ph= "120092340980",email="first@adda.com")
    app.contact.create_c(contacts)
    assert len(old_contact)+1 == app.contact.count_first()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contacts)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

