__author__ = 'Sergei'

def test_group_edit(app):
    app.session.login(username= "admin",password="secret")
    app.group.test_edit_group()
    app.session.logout()