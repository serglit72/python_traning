__author__ = 'Sergei'
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact_first_last(self, Contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contact.first_n)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contact.last_n)

    def create_first_last(self, Contact):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_first_last(Contact)

        if wd.find_element_by_name("submit").click():
            wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_full(self, Contact):
        wd = self.app.wd
        self.change_field_value("firstname",Contact.first_n)
        self.change_field_value("middlename",Contact.mid_n)
        self.change_field_value("lastname",Contact.last_n)
        self.change_field_value("nickname",Contact.nick_n)
        self.change_field_value("company",Contact.company)
        self.change_field_value("address",Contact.address)
        self.change_field_value("home",Contact.home_ph)
        self.change_field_value("mobile",Contact.cell_ph)
        self.change_field_value("email",Contact.email)

    def create_c(self,contacts):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_full(contacts)
        if wd.find_element_by_name("submit").click():
            wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contact_cache = None


    def select_contact_by_index(self,index):
        wd = self.app.wd
#        self.open_contact_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("http://localhost/addressbook/")):
            wd.get("http://localhost/addressbook/")

    def contact_delete_by_index(self,index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        wd.find_element_by_name("update[value=\"Delete\"]").click()
#        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
#        wd.switch_to_alert().accept()
        self.contact_cache = None

    def contact_modify_by_index(self,index,cont):
        wd = self.app.wd
 #       self.open_contact_page()
        self.select_contact_by_index(index)
#        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.fill_first_last_name(cont)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contact_cache = None


    def fill_first_last_name(self, Contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contact.first_n)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contact.last_n)

    def modify_first_contact(self, cont, index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
     #  wd.find_element_by_css_selector("img[alt=\"Edit\"]")[index].click()
        self.fill_first_last_name(cont)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contact_cache = None

    def contact_delete(self):
        self.contact_delete_by_index(0)
        self.contact_cache = None

    def contact_first_modify(self):
        self.contact_modify_by_index(0)
        self.contact_cache = None


    def test_edit_contact(self, Contact):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        self.fill_contact_full(Contact)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contact_cache = None


    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def count_first(self):
        wd = self.app.wd
        self.open_contact_page()
#        wd.find_elements_by_name('entry')
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name('entry'):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                text = element.text
                self.contact_cache.append(Contact( id=id, first_n=text))
        return list(self.contact_cache)

