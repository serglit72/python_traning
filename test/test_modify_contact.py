__author__ = 'Sergei'

from model.contact import Contact

def test_contact_edit(app):
    if app.contact.count() == 0:
        app.contact.create_c(Contact(first_n= "first",mid_n= "middle",last_n= "last",nick_n= "kuk",company= "adda",address= "575 oiweojdckjgsd,russia",home_ph= "12134519827",
                cell_ph= "120092340980",email= "first.lastmiddle.@adda.com"))
    old_contact = app.contact.get_contact_list()
    app.contact.test_edit_contact()
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
