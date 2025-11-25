from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_login(page):

    home = HomePage(page)
    login = LoginPage(page)

    # Navigate to Login Page
    home.go_to_site()
    home.click_link("Form Authentication")

    # --- Invalid Password Test ---
    login.login("tomsmith", "SuperSecretPassword")
    login.verify_banner_contains("Your password is invalid!")  # partial match allowed

    # --- Valid Login Test ---
    login.login("tomsmith", "SuperSecretPassword!")
    login.verify_login_success("You logged into a secure area!")

    # --- Logout Test ---
    login.logout()
    login.verify_logout_success("You logged out of the secure area!")
