import time

from playwright.sync_api import sync_playwright

from pages.example_page import ExamplePage


def test_example_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)

        # Create a browser context with geolocation permission
        context = browser.new_context(
            permissions=["geolocation"]
        )

        # Open a new page in that context
        page = context.new_page()
        example = ExamplePage(page)
        example.open()

        # Verify page title contains "Carteav"
        assert "Carteav" in example.title()
        print("✅ Page opened successfully")

        time.sleep(3)

        # Click 'Move to Testing User'
        example.click_move_to_testing_user()
        time.sleep(7)

        # Open the POI dropdown
        example.open_poi_dropdown()
        time.sleep(2)

        # Select the first station ('Spa sababa')
        example.click_move_to_spa_sababa()
        time.sleep(2)

        # Click "הזמן רכב"
        example.click_order_vehicle()
        time.sleep(3)

        # Click "התחל נסיעה"
        example.click_start_driving()
        time.sleep(3)

        # Keep the browser open so you can see what happened
        input("🟢 Browser is open. Press Enter in console to close, and see test results")

        # Close the browser
        browser.close()
        print("✅ Browser closed")
