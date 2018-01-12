from behave import *
from nose.tools import *
from selenium.webdriver.common.by import By

@given(u'I am on the shopping website')
def step_impl(context):
    context.home_page.is_header_present()

@when(u'I search for "{search_term}"')
def step_impl(context, search_term):
    context.home_page.search(search_term)
    context.home_page.search(u'\ue007')

@then(u'I should get the search results for winter coat')
def step_impl(context):
    context.search_page.verify_search_results()


# @given(u'I navigate to the PyPi Home page')
# def step_impl(context):
#     context.home_page.navigate("https://pypi.python.org/pypi")
#     assert_equal(context.home_page.get_page_title(), "PyPI - the Python Package Index : Python Package Index")
#
# @when(u'I search for "{search_term}"')
# def step_impl(context, search_term):
#     context.home_page.search(search_term)
#
# @then(u'I am taken to the PyPi Search Results page')
# def step_impl(context):
#     assert_equal(context.search_page.get_page_title(), "Index of Packages Matching 'behave' : Python Package Index")
#
# @then(u'I see a search result "{search_result}"')
# def step_impl(context, search_result):
#     assert_true(context.search_page.find_search_result(search_result))