from pytest_bdd import given, when, then, parsers, scenarios

scenarios('..')


@given(parsers.parse('на странице "{page}"'))
async def step_navigate(page_obj, page):
    await page_obj.navigate(page)


@when(parsers.parse('ввожу в "{element}" текст "{value}"'))
async def step_fill(page_obj, value, element):
    await page_obj.fill(element, value)


@when(parsers.parse('кликаю "{element}"'))
async def step_click(page_obj, element):
    await page_obj.click(element)


@then(parsers.parse('вижу "{element}"'))
async def step_visible(page_obj, element):
    assert await page_obj.is_visible(element)


@then(parsers.parse('в "{element}" текст "{expected}"'))
async def step_text(page_obj, expected, element):
    actual = await page_obj.get_text(element)
    assert expected in actual, f'Ожидалось "{expected}", получено "{actual}"'


@then(parsers.parse('URL содержит "{part}"'))
async def step_url(page, part):
    assert part in page.url
