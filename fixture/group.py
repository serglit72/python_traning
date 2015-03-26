__author__ = 'Sergei'

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self,group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
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
        self.return_to_group_page()

    def del_first_group(self):
         wd = self.app.wd
         self.open_groups_page()
        #select group
         wd.find_element_by_name("selected[]").click()
        #delete group
         wd.find_element_by_name("delete").click()


    def return_to_group_page(self):
        # return to groups page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def test_edit_group(self):
        wd = self.app.wd
    #    wd.get("http://localhost/addressbook/")
        self.open_groups_page()
        wd.find_element_by_xpath("//div[@id='content']/form/input[6]").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("Groupe5")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("dfghdghjdghj")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("wertwer")
        wd.find_element_by_name("update").click()
        self.return_to_group_page()