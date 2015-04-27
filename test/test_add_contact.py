__author__ = 'Sergei'
from model.contact import Contact

def test_contact_new(app):
    old_contact = app.contact.get_contact_list()
    app.contact.create_c(Contact(first_n="First",mid_n="middle",last_n="last",nick_n= "kuk",company= "adda",address= "575 oiweojdckjgsd,russia",home_ph= "12134519827",
    cell_ph= "120092340980",email= "first.lastmiddle.@adda.com"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact)+1 == len(new_contact)



#    assert len(old_contact)+1 == app.contact.count_first()
 #   new_contact = app.contact.get_contact_list()
 #   old_contact.append(contact_first)
 #   assert sorted(old_contact, key= Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
