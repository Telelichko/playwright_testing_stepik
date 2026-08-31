from pytest_bdd import given, when, then, parsers, scenarios

scenarios("./login.feature")

# ---------- Steps (no async, no await) ----------

@given(parsers.parse('на странице "{url}"'))
def step_navigate(page, url: str):
    # Adjust base URL as needed – or use a fixture
    page.goto(f"https://example.com/{url}")

@when(parsers.parse('ввожу в "{element}" текст "{value}"'))
def step_fill(page, element: str, value: str):
    page.fill(element, value)

@when(parsers.parse('кликаю "{element}"'))
def step_click(page, element: str):
    page.click(element)

@then(parsers.parse('вижу "{element}"'))
def step_visible(page, element: str):
    assert page.is_visible(element), f"Element '{element}' is not visible"

@then(parsers.parse('в "{element}" текст "{expected}"'))
def step_text(page, element: str, expected: str):
    actual = page.text_content(element) or ""
    assert expected in actual, f'Expected "{expected}" in "{actual}"'

@then(parsers.parse('URL содержит "{part}"'))
def step_url(page, part: str):
    assert part in page.url