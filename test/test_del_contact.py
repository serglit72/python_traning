__author__ = 'Sergei'


def test_del_contact(app):
    app.session.login(username= "admin",password="secret")
    app.contact.contact_delete()
    app.session.logout()
