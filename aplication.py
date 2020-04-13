from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(50)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://coredemo.apdow.net/")

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element(By.LINK_TEXT, "Sign In").click()
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").send_keys("79210120011")
        wd.find_element(By.NAME, "password").send_keys("Anika777")
        wd.find_element(By.CSS_SELECTOR, ".green").click()

    def logout(self):
        wd = self.wd
        wd.find_element(By.CSS_SELECTOR, ".ng-tns-c22-3 .ready").click()
        wd.find_element(By.LINK_TEXT, "Выйти").click()

    def destroy(self):
        self.wd.quit

