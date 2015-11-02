from selenium import webdriver
import pytest


def test_selenium_basic():
    driver = webdriver.PhantomJS()
    urlstr = "http://localhost:5000/"
    driver.get(urlstr)
    assert driver.current_url == urlstr
    bod = driver.find_element_by_tag_name('body')
    assert "Hello" in bod.text

    driver.quit()
