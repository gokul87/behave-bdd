from selenium import webdriver
from features.browser import Browser
from features.pages.search_home_page import SearchHomePage
from features.pages.search_results_page import SearchResultsPage


def before_all(context):
    context.browser = Browser()
    context.home_page = SearchHomePage()
    context.search_page = SearchResultsPage()


def after_all(context):
    context.browser.close()