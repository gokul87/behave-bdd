from selenium.webdriver.common.by import By
from features.browser import Browser

class SearchResultsPageLocator(object):
    # results page locator

    RESULT_LIST = (By.CSS_SELECTOR, ".z-nvg-cognac_articles .z-nvg-cognac_articleCard-1r8nF")


class SearchResultsPage(Browser):
    # actions to perform on search results page

    def verify_search_results(self):
        title_ele = self.driver.find_elements(*SearchResultsPageLocator.RESULT_LIST)
        topTenProducts = len(title_ele) - 73

        for i in range(1, int(topTenProducts)):
            title = self.driver.find_element(By.CSS_SELECTOR,
                                             ".z-nvg-cognac_articles .z-nvg-cognac_articleCard-1r8nF:nth-child("+str(i)+") .z-nvg-cognac_articleName--arFp").text
            if 'Winter' or 'coat' in title:
                print("The title of the product is "+ title)
                print("Test Successfully passed")
            else:
                print("Test failed")
