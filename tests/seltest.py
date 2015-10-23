from selenium import webdriver
import pytest


def test_selenium_basic():
    driver = webdriver.Firefox()
    driver.get("localhost:5000")
    bod = driver.get_element_by_tag_name('body')
    assert "Hello" in bod.text

    driver.quit()
