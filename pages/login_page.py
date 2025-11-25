from playwright.sync_api import expect


class LoginPage:
    def __init__(self, page):
        self.page = page

        # Locators
        self.heading_h2 = page.locator("h2")
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.logout_button = page.locator("a[href='/logout']")
        self.secure_area_title = page.locator("h2:has-text('Secure Area')")
        self.banner_flash = page.locator("#flash")

    # ------------------------------
    # Generic Helpers
    # ------------------------------
    def get_banner_message(self):
        """Returns the flash banner text (trimmed)."""
        return self.banner_flash.inner_text().strip()

    def verify_banner_contains(self, expected_text: str):
        """Generic banner validation method."""
        expect(self.banner_flash).to_contain_text(expected_text)
        assert (
            expected_text in self.get_banner_message()
        ), f"Expected '{expected_text}', but got '{self.get_banner_message()}'"

    # ------------------------------
    # Login Actions
    # ------------------------------
    def login(self, username: str, password: str):
        """Performs login action."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def verify_login_success(self, expected_message: str):
        """Verifies user successfully logged in."""
        expect(self.secure_area_title).to_be_visible()
        self.verify_banner_contains(expected_message)

    # ------------------------------
    # Logout Actions
    # ------------------------------
    def logout(self):
        """Clicks the logout button after successful login."""
        expect(self.secure_area_title).to_be_visible()
        self.logout_button.click()

    def verify_logout_success(self, expected_message: str):
        """Verifies user successfully logged out."""
        self.verify_banner_contains(expected_message)
