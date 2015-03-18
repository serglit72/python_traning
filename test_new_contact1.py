# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest

from group import Groups

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_new_contact(unittest.TestCase):
    def setUp(self):
            self.wd = WebDriver()
            self.wd.implicitly_wait(60)
    def open_home_page(self, wd):
            wd.get("http://localhost/addressbook/")
    def login(self, wd, username, password):
            wd.find_element_by_name("user").click()
            wd.find_element_by_name("user").clear()
            wd.find_element_by_name("user").send_keys(username)
            wd.find_element_by_id("LoginForm").click()
            ActionChains(wd).double_click(wd.find_element_by_id("LoginForm")).perform()
            wd.find_element_by_name("pass").click()
            wd.find_element_by_name("pass").clear()
            wd.find_element_by_name("pass").send_keys(password)
            wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def init_new_contact(self, wd):
             wd.find_element_by_link_text("add new").click()

    def fill_form(self, wd, Groups):
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(Groups.first_n)
            wd.find_element_by_name("middlename").click()
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(Groups.midd_n)
            wd.find_element_by_name("lastname").click()
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(Groups.last_n)
            wd.find_element_by_name("nickname").click()
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(Groups.nick_n)
            wd.find_element_by_name("company").click()
            wd.find_element_by_name("company").clear()
            wd.find_element_by_name("company").send_keys(Groups.company)
            wd.find_element_by_name("address").click()
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(Groups.address)
            wd.find_element_by_name("theform").click()
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(Groups.home_ph)
            wd.find_element_by_name("mobile").click()
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(Groups.cell_ph)
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(Groups.email)

    def fill_drop_down_boxes(self, wd):
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()

    def fill_end_form(self, wd):
            wd.find_element_by_name("byear").click()
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys("1970")

    def enter(self, wd):
            wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def logout(self, wd):
            wd.find_element_by_link_text("Logout").click()

    def test_test_new_contact(self):
            success = True
            wd = self.wd
            self.open_home_page(wd)
            self.login(wd, username="admin",password= "secret")
            self.init_new_contact(wd)
            self.fill_form(wd, Groups(first_n= "first",midd_n= "middle",last_n= "last",nick_n= "kuk",company= "adda",address= "575 oiweojdckjgsd,russia",home_ph= "12134519827",
                cell_ph= "120092340980",email= "first.lastmiddle.@adda.com"))
            self.fill_drop_down_boxes(wd)
            self.fill_end_form(wd)
            self.enter(wd)
            self.logout(wd)
            self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
