import pytest
from selenium import webdriver
import time

def test_button_add_to_basket(browser):
	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
	browser.get(link)
	browser.find_element_by_css_selector('button.btn-add-to-basket')
