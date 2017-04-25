from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

import unittest

class nova_poshta(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(5)
    
    def test_nova_poshta(self):
        success = True
        wd = self.wd
        wd.get("https://novaposhta.ua/")

        wd.find_element(By.ID, 'cargo_number').click()
        wd.find_element_by_id("cargo_number").clear()

        elem = wd.find_element_by_id("cargo_number")
        elem.send_keys("59000251696064")
        elem.send_keys(Keys.ENTER)

        # screenshot
        wd.save_screenshot('screenshot.png')

        # ActionChains работает
        menu = wd.find_element_by_css_selector('#top_menu > li:nth-child(5) > a')
        submenu = wd.find_element_by_css_selector('#top_menu > li:nth-child(5) > ul > li:nth-child(1) > a')
        action = ActionChains(wd)
        action.move_to_element(menu).perform()
        time.sleep(1)
        action.click(submenu).perform()
        time.sleep(2)

        # еще не исправлено
        wd.find_element_by_xpath('//*[@id="i_City"]').click()
        wd.find_element_by_xpath('//*[@id="i_City"]').clear()
        wd.find_element_by_xpath('//*[@id="i_City"]').send_keys("ки")
        wd.find_element_by_css_selector("li.Київ.hover").click()
        wd.find_element_by_id("i_Office_num").click()
        wd.find_element_by_xpath("//div[@class='dropdown']//li[.='Всі типи']").click()
        wd.find_element_by_css_selector("li.Київ.active").click()
        wd.find_element_by_id("i_Office_num").click()
        wd.find_element_by_id("i_Office_num").clear()
        wd.find_element_by_id("i_Office_num").send_keys("25")
        wd.find_element_by_xpath("//div[@class='dropdown']//li[.='Всі типи']").click()
        wd.find_element_by_xpath("//div[@class='jspPane']//span[.='Відділення №25']").click()
        wd.find_element_by_xpath("//div[@class='option_select']//span[.='Всі типи']").click()
        wd.find_element_by_xpath("//li[@class='hover']//span[.='Вантажні відділення']").click()
        wd.find_element_by_id("i_Office_num").click()
        wd.find_element_by_xpath("//div[@class='jspPane']//li[.='Відділення №25']").click()
        wd.find_element_by_link_text("Контакти").click()
        wd.find_element_by_link_text("Зворотний зв’язок").click()
        wd.find_element_by_xpath("//div[@id='wrapper']//i[.='Перейти вгору']").click()
        self.assertTrue(success)
    
    def tearDown(self):
        pass
        # self.wd.quit()

if __name__ == '__main__':
    unittest.main()
