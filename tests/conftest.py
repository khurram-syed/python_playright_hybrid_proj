import pytest
import os
from playwright.sync_api import Playwright, sync_playwright


@pytest.fixture(scope="session")
def page():
    # Detect if code is running in CI (GitHub Actions sets CI=true)
    is_ci = os.getenv("CI", "false").lower() == "true"
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=is_ci)  # Headless in CI, headed locally
        context = browser.new_context()
        page = context.new_page()

        yield page

        browser.close()
