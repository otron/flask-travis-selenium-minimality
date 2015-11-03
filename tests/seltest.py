from selenium import webdriver
import pytest
import os


def init_browser_via_env_var(env_str='SELTEST_BROWSER'):
    """Returns a webdriver instance of the browser specified by the
    `env_str` arg."""
    try:
        browser_nm = os.environ[env_str]
        # os.environ[key] raises a KeyError if the env. var doesn't exist
    except KeyError:
        browser_nm = 'PhantomJS'
    finally:
        return getattr(webdriver, browser_nm)()


def test_selenium_basic():
    driver = init_browser_via_env_var()
    urlstr = "http://localhost:5000/"
    driver.get(urlstr)
    assert driver.current_url == urlstr
    bod = driver.find_element_by_tag_name('body')
    assert "Hello" in bod.text

    driver.quit()
