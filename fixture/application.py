

__author__ = 'Sergei'
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)


    def open_home_page(self):
        # open home page
       wd = self.wd
       wd.get("http://localhost/addressbook/group.php")


    def open_groups_page(self):
        # open group page
        wd = self.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()


    def create_fill_group_form(self,group):
        # create and fill group form
        wd = self.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        #submit group creation
        wd.find_element_by_name("submit").click()
        self.open_groups_page()
        self.return_to_group_page()


    def return_to_group_page(self):
        # return to groups page
        wd = self.wd
        wd.find_element_by_link_text("group page").click()


    def destroy(self):
        self.wd.quit()

