from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
from Packages.Interactions import like_comment, like_comment_commentadors, like_comment_automatic

class instagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_linguages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(firefox_profile=firefoxProfile, executable_path=r"/usr/local/bin/geckodriver")
    
    def login(self, comment=False, hashtag=False, commentadors=False, automatic=False):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        sleep(random.randint(4, 10))
        driver.maximize_window()
        driver.find_element_by_name("username").send_keys(self.username)
        driver.find_element_by_name("password").send_keys(self.password)
        button = driver.find_element_by_css_selector(".L3NKy")
        button.send_keys(Keys.RETURN)
        sleep(4)
        if automatic:
            like_comment_automatic(self)
        elif commentadors:
            like_comment_commentadors(self, comment, hashtag)
        else:
            like_comment(self, comment, hashtag)
        fim = random.choice([True, False])
        if fim:
            driver.find_element_by_xpath("//a[@href='/']").click()
        else:
            driver.find_element_by_css_selector("._6q-tv").click()
            driver.find_element_by_xpath("//*[contains(text(), 'Perfil')]").click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(random.randint(1, 4))
        driver.find_element_by_css_selector("._6q-tv").click()
        driver.find_element_by_xpath("//*[contains(text(), 'Sair')]").click()
        sleep(random.randint(2, 5))
        driver.quit()

#test = instagram("username", "password")
#test.login()