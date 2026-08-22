# features/conftest.py
import pytest
from pytest_bdd import scenarios
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=False)
    yield browser
    browser.close()
    pw.stop()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
