

def test_addcomment(self):

    self.driver.get("https://coredemo.apdow.net/")
    self.driver.set_window_size(2490, 1376)
    self.driver.find_element(By.LINK_TEXT, "Sign In").click()
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("79210120011")
    self.driver.find_element(By.NAME, "password").send_keys("Anika777")
    self.driver.find_element(By.CSS_SELECTOR, ".green").click()
    self.driver.find_element(By.LINK_TEXT, "Свежее").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c125-12 > .lazyautosizes").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-invalid").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-dirty").send_keys("Test_1")
    self.driver.find_element(By.CSS_SELECTOR, ".fa-paper-plane > path").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c22-3 .ready").click()
    self.driver.find_element(By.LINK_TEXT, "Выйти").click()
...


def test_addcomment(self):

    self.driver.get("https://coredemo.apdow.net/")
    self.driver.set_window_size(2490, 1376)
    self.driver.find_element(By.LINK_TEXT, "Sign In").click()
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("79210120011")
    self.driver.find_element(By.NAME, "password").send_keys("Anika777")
    self.driver.find_element(By.CSS_SELECTOR, ".green").click()
    self.driver.find_element(By.LINK_TEXT, "Свежее").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c125-12 > .lazyautosizes").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-invalid").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-dirty").send_keys("Test_1")
    self.driver.find_element(By.CSS_SELECTOR, ".fa-paper-plane > path").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c22-3 .ready").click()
    self.driver.find_element(By.LINK_TEXT, "Выйти").click()

