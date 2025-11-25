from pages.home_page import HomePage
from playwright.sync_api import expect


def test_home_page(page):
    home = HomePage(page)

    # Navigate to HomePage
    home.go_to_site()

    # Validate title
    expect(page).to_have_title("The Internet")

    # Validate heading text
    expect(home.heading_h1).to_have_text("Welcome to the-internet")
