__author__ = 'Sergei'

from model.contact import Contact
from random import randrange

def test_contact_modify(app):
    cont = Contact(first_n= "FIRST",last_n= "LAST")
    if app.contact.count() == 0:
        app.contact.create_c(Contact(first_n= "first",mid_n= "middle",last_n= "last",nick_n= "kuk",company= "adda",address= "575 oiweojdckjgsd,russia",home_ph= "12134519827",
        cell_ph= "120092340980",email= "first.lastmiddle.@adda.com"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    app.contact.modify_first_contact(cont, index)
    cont.id = old_contact[index].id
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    new_contact_1 = new_contact.split()
    new_contact=new_contact_1[0:3]
    old_contact[index]= cont
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


#    index = randrange(len(old_contact))
#    app.contact.contact_modify_by_index(index, cont)
#    cont.id = old_contact[index].id
#    app.contact.modify_first_contact(Contact(first_n="Second"))
#    app.contact.test_edit_contact(cont)
#    new_contact = app.contact.get_contact_list()
#    assert len(old_contact) == len(new_contact)
#    old_contact[index]= cont
 #   assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)***