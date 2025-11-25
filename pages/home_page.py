from playwright.sync_api import expect


class HomePage:
    def __init__(self, page):
        self.page = page

        # Locators
        self.heading_h1 = page.locator("h1")
        self.menu_links = page.locator("ul li a")  # Generic links list
        self.base_url = "https://the-internet.herokuapp.com/"

    # --------------------------------
    # Navigation
    # --------------------------------
    def go_to_site(self):
        """Navigate to the main site."""
        self.page.goto(self.base_url)
        expect(self.heading_h1).to_be_visible()

    # --------------------------------
    # Header
    # --------------------------------
    def get_heading(self) -> str:
        """Return the top page heading text."""
        return self.heading_h1.inner_text().strip()

    # --------------------------------
    # Generic Link Click
    # --------------------------------
    def click_link(self, link_text: str):
        """
        Clicks a link by visible text on the home page.
        Using :has-text() ensures accurate matching.
        """
        locator = self.page.locator(f"a:has-text('{link_text}')")
        expect(locator).to_be_visible()
        locator.click()
