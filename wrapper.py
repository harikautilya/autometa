from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminAutomate():
    admin_url = ""

    def __init__(self, admin_url="", username="", password="", delay=10):
        self.admin_url = admin_url
        self.driver = webdriver.Safari()
        self.driver.set_window_size(1000, 3000)
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_url)
        self.delay = delay
        self.time = time
        self.logging_file = open("logger.txt", "w")
        enter_username = self.find_element_by_id("username")
        enter_password = self.find_element_by_id("password")
        self.enter_value(enter_username, username)
        self.enter_value(enter_password, password)
        enter_password.send_keys(Keys.RETURN)
        self.page_is_loading()

    def delay_page(self, secs=0):
        time.sleep(secs)

    def page_is_loading(self):
        self.delay_page(secs=5)
        # while True:
        #     self.time.sleep(1)
        #     x = self.driver.execute_script("return document.readyState")
        #     if x == "complete":
        #         return True
        #     else:
        #         yield False

    # this method is not working
    def wait_for_id(self, id=""):
        WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.ID, id)))

    def log(self, log_data):
        self.logger_file.write("\n")
        self.logger_file.write(str(log_data))
        print(log_data)

    def get_column_value(self, column=""):
        return self.find_element_by_id(column).get_attribute("value")

    def write_to_column(self, column="", value=""):
        column_id = self.find_element_by_id(column)
        actions = ActionChains(self.driver)
        actions.move_to_element(column_id).perform()
        self.enter_value(column_id, str(value))

    def add_model(self, app="", table=""):
        url = "{admin_url}{app}/{table}/add/".format(admin_url=self.admin_url, app=app, table=table)
        self.driver.get(url)
        self.page_is_loading()

    def navigate_to_table_with_key(self, app="", table="", key=""):
        url = "{admin_url}{app}/{table}/{key}/".format(admin_url=self.admin_url, app=app, table=table, key=key)
        self.driver.get(url)
        self.page_is_loading()

    def navigate_to_table(self, app="", table=""):
        url = "{admin_url}{app}/{table}/".format(admin_url=self.admin_url, app=app, table=table)
        self.driver.get(url)
        self.page_is_loading()

    def check_column(self, column=""):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "id_{column}".format(column=column))))
        self.find_element_by_id(id=column).click()

    def find_element_by_id(self, id=""):
        return self.driver.find_element_by_id("id_{id}".format(id=id))

    def enter_value(self, element=None, value=""):
        if element is None:
            raise Exception("Element cannot be null")
        element.send_keys(value)
   

    def close(self):
        self.driver.quit()
