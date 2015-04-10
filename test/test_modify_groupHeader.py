__author__ = 'Sergei'
from model.group import Group


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="test"))
    app.group.modify_first_group(Group(header="New++ header++"))

