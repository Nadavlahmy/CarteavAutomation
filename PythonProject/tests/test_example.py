import time
from playwright.sync_api import sync_playwright
from pages.example_page import ExamplePage

def test_example_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)

        # ✅ Create a context with browser permission granted
        # Replace "geolocation" with "notifications" if the popup is notifications
        context = browser.new_context(
            permissions=["geolocation"]
        )

        # Open a new page in the context
        page = context.new_page()
        example = ExamplePage(page)
        example.open()

        # Verify page title contains "Carteav"
        assert "Carteav" in example.title()
        print("✅ Page opened successfully")

        time.sleep(3)

        # Click Move to Testing User button
        example.click_move_to_testing_user()
        print("➡ Clicked 'Move to Testing User'")

        # Keep browser open to verify the action
        input("🟢 Browser is open. Press Enter to close, and see test results")

        # Close browser
        browser.close()
        print("✅ Browser closed")
