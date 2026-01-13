from playwright.sync_api import sync_playwright
from pages.example_page import ExamplePage

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()

        example = ExamplePage(page)
        example.open()

        print("This is an automated reservation app method")
        print("Browser is open. You can interact with the page.")
        input("Press Enter to close the browser...")
        example.click_move_to_testing_user()


        browser.close()

        print("Browser closed.")

if __name__ == "__main__":
    main()

