import yaml
from pathlib import Path
import pytest
from pytest_bdd import given, when, then, parsers, scenarios
from playwright.sync_api import Page


scenarios('./login.feature')

PATH_CONFIG_FOLDER = '././config'

with open(f'{PATH_CONFIG_FOLDER}/pages.yaml', encoding='utf-8') as f:
    pages_data = yaml.safe_load(f)

with open(f'{PATH_CONFIG_FOLDER}/elements.yaml', encoding='utf-8') as f:
    elements_data = yaml.safe_load(f)

CONFIG = {
    'config': pages_data['config'],
    'pages': pages_data['pages'],
    'elements': elements_data['elements']
}

BASE_URL = CONFIG['config']['base_url']
PAGES = CONFIG['pages']
ELEMENTS = CONFIG['elements']


@given(parsers.parse('на странице "{page_name}"'))
def step_navigate(page: Page, page_name: str):
    page.goto(BASE_URL + PAGES[page_name]['path'])
    page.wait_for_load_state('networkidle')

@when(parsers.parse('ввожу в "{element_name}" текст "{text}"'))
def step_fill(page: Page, element_name: str, text: str):
    page.fill(ELEMENTS[element_name]['selector'], text)

@when(parsers.parse('кликаю "{element_name}"'))
def step_click(page: Page, element_name: str):
    page.click(ELEMENTS[element_name]['selector'])

@then(parsers.parse('URL содержит "{expected}"'))
def step_url_contains(page: Page, expected: str):
    assert expected in page.url, f'Expected value "{expected}" not found in URL "{page.url}"'
