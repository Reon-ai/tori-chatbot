# conftest.py for pytest
import pytest

# Ensure asyncio mode is set for async tests
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "asyncio: mark test as async"
    )
