from time import sleep

from selenium.webdriver.common.by import By
from features.browser import Browser

class SearchHomePageLocator(object):
    # list the locators for home page

    HEADER_ICON = (By.CSS_SELECTOR, ".z-navicat-header_logoLinkWrapper")
    SEARCH_BOX = (By.CSS_SELECTOR, ".z-navicat-header_searchInput")

    # HEADER_TEXT = (By.XPATH, "//h1")
    # SEARCH_TEXT = (By.ID, "term")
    # SUBMIT_BTN = (By.ID, "submit")

class SearchHomePage(Browser):
    # actions to perform on home page

    def is_present(self, *locator):
        return self.driver.find_element(*locator).is_displayed()

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def is_header_present(self):
        self.is_present(*SearchHomePageLocator.HEADER_ICON)

    def search(self, search_term):
        # self.fill(search_term, *SearchHomePageLocator.SEARCH_BOX)
        # sleep(1)
        if(self.is_present(*SearchHomePageLocator.SEARCH_BOX)):
            print("I am here")
            self.fill(search_term, *SearchHomePageLocator.SEARCH_BOX)
            sleep(1)
        else:
            print("Condition failed")
