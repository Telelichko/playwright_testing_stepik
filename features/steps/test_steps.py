from pytest_bdd import given, when, then, parsers, scenarios

scenarios(".")

# ---------- Steps ----------

@given(parsers.parse('на странице "{url}"'))
async def step_navigate(page, url: str):
    """Open a specific page (relative to base URL)."""
    # Ideally, use a base URL from a fixture or environment variable
    await page.goto(f"https://example.com/{url}")

@when(parsers.parse('ввожу в "{element}" текст "{value}"'))
async def step_fill(page, element: str, value: str):
    """Fill an input field."""
    await page.fill(element, value)

@when(parsers.parse('кликаю "{element}"'))
async def step_click(page, element: str):
    """Click on an element."""
    await page.click(element)

@then(parsers.parse('вижу "{element}"'))
async def step_visible(page, element: str):
    """Check that an element is visible."""
    assert await page.is_visible(element), f"Element '{element}' is not visible"

@then(parsers.parse('в "{element}" текст "{expected}"'))
async def step_text(page, element: str, expected: str):
    """Check that an element's text contains the expected substring."""
    actual = await page.text_content(element)
    assert expected in (actual or ""), f'Expected "{expected}" in "{actual}"'

@then(parsers.parse('URL содержит "{part}"'))
async def step_url(page, part: str):
    """Check that the current URL contains the given part."""
    assert part in page.url
