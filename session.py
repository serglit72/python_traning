__author__ = 'Sergei'

class SessionHelper:

    def __init__(self, app):
        self.app = app




    def logout(self):
        # logout
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
