# features/conftest.py
import pytest
from pytest_bdd import scenarios
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='session')
def browser():
    '''Launches a session-scoped headed Chromium browser instance.'''
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=False)
    yield browser
    browser.close()
    pw.stop()

@pytest.fixture
def page(browser):
    '''Creates a new isolated browser context and page for each test.'''
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
