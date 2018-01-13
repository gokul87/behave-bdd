from selenium import webdriver

class Browser(object):

    baseurl = "https://www.zalando.co.uk/"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    chrome_options.add_argument("window-size=1200x600")
    driver = webdriver.Chrome(executable_path='./drivers/chromedriver_new',
                              chrome_options=chrome_options)


    driver.set_page_load_timeout(10)
    driver.get(baseurl)
    driver.implicitly_wait(10)
    #driver.maximize_window()

    def close(self):
        self.driver.quit()