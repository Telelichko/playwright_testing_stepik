import pytest


@pytest.fixture(scope='session')
def event_loop():
    """Provides a single session-scoped asyncio event loop for async tests."""
    import asyncio
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

def pytest_collection_modifyitems(items):
    """Automatically applies the asyncio marker to pytest-bdd scenarios."""
    for item in items:
        if "scenario" in item.fixturenames or "feature" in item.fixturenames:
            item.add_marker(pytest.mark.asyncio)
