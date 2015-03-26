__author__ = 'Sergei'

def test_contact_edit(app):
    app.session.login(username= "admin",password="secret")
    app.contact.test_edit_contact()
    app.session.logout()
