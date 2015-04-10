__author__ = 'Sergei'
from model.group import Group


def test_group_edit(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.test_edit_group()
