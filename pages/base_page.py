# !pip install playwright
# !playwright install
# !pip install PyYAML

import yaml
from pathlib import Path
from playwright.async_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.pages_config = self._load_config('pages.yaml')
        self.elements_config = self._load_config('elements.yaml')

    def _load_config(self, filename: str) -> dict:
        """Load configuration file"""
        config_path = Path(__file__).parent.parent / 'config' / filename
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def get_page_url(self, page_name: str) -> str:
        """Get page URL by name"""
        page_name = page_name.lower().strip()
        if page_name in self.pages_config['pages']:
            return self.pages_config['pages'][page_name]['url']
        raise ValueError(f'Page "{page_name}" not found in configuration')

    def get_element_selector(self, element_name: str) -> str:
        """Get element selector by name"""
        element_name = element_name.lower().strip().replace(' ', '_')
        if element_name in self.elements_config['elements']:
            return self.elements_config['elements'][element_name]['selector']
        raise ValueError(f'Element "{element_name}" not found in configuration')

    def get_element_type(self, element_name: str) -> str:
        """Get element type"""
        element_name = element_name.lower().strip().replace(' ', '_')
        return self.elements_config['elements'][element_name].get('type', 'unknown')

    async def navigate_to(self, page_name: str):
        """Navigate to page by name"""
        url = self.get_page_url(page_name)
        await self.page.goto(url)
        await self.page.wait_for_load_state('networkidle')

    async def click_element(self, element_name: str):
        """Click element by name"""
        selector = self.get_element_selector(element_name)
        await self.page.locator(selector).click()

    async def fill_field(self, element_name: str, value: str):
        """Fill field by name"""
        selector = self.get_element_selector(element_name)
        await self.page.locator(selector).fill(value)

    async def get_text(self, element_name: str) -> str:
        """Get element text by name"""
        selector = self.get_element_selector(element_name)
        await self.page.locator(selector).wait_for(state='visible')
        return await self.page.locator(selector).text_content()

    async def is_visible(self, element_name: str) -> bool:
        """Check element visibility"""
        selector = self.get_element_selector(element_name)
        return await self.page.locator(selector).is_visible()

    async def wait_for_element(self, element_name: str, timeout: int = 5000):
        """Wait for element to appear"""
        selector = self.get_element_selector(element_name)
        await self.page.locator(selector).wait_for(state='visible', timeout=timeout)
