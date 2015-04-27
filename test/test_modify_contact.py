__author__ = 'Sergei'

from model.contact import Contact

def test_contact_edit(app):
    cont = Contact(first_n= "first",mid_n= "middle",last_n= "last",nick_n= "kuk",company= "adda",address= "575 oiweojdckjgsd,russia",home_ph= "12134519827",
    cell_ph= "120092340980",email= "first.lastmiddle.@adda.com")
    if app.contact.count() == 0:
        app.contact.create_c(cont)
    old_contact = app.contact.get_contact_list()
    cont.id = old_contact[0].id
    app.contact.test_edit_contact(cont)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
 #   old_contact[0]= cont
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)