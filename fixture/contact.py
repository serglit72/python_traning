__author__ = 'Sergei'
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app


    def create_c(self, Contact):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contact.first_n)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Contact.mid_n)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contact.last_n)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Contact.nick_n)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(Contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(Contact.address)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Contact.home_ph)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Contact.cell_ph)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(Contact.email)
 #       if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
 #           wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
  #      if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
  #          wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("Russian Federation")
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("S- Petersburg")
        if wd.find_element_by_name("submit").click():
            wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()


    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("http://localhost/addressbook/")):
            wd.get("http://localhost/addressbook/")

    def contact_delete(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def test_edit_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("FIRST_NAME221")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("LAST_NAME332")
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("Russia")
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("Moscow city")
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()


    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def count_first(self):
        wd = self.app.wd
        self.open_contact_page()
#        wd.find_elements_by_name('entry')
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contact_page()
        contacts = []
        for element in wd.find_elements_by_name('entry'):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(first_n=text, id=id))
        return contacts

#    contact_cache = None

#    def get_contact_list(self):
#        if self.contact_cache is None:
#            wd = self.app.wd
#            self.open_contact_page()
#            self.contact_cache = []
#            for element in wd.find_elements_by_name('entry'):
#                text = element.text
#                id = element.find_element_by_name("selected[]").get_attribute("value")
#                self.contact_cache.append(Contact(id=id,first_n=text))
 #       return list(self.contact_cache)


