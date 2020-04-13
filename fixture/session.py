from selenium.webdriver.common.by import By

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.LINK_TEXT, "Sign In").click()
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").send_keys("79210120011")
        wd.find_element(By.NAME, "password").send_keys("Anika777")
        wd.find_element(By.CSS_SELECTOR, ".green").click()


    def logout(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "div.user-avatar").click()
        wd.find_element(By.LINK_TEXT, "Выйти").click()