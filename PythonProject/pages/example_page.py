from playwright.sync_api import Page

class ExamplePage:
    URL = "https://office.carteav.com"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def click_move_to_testing_user(self):
        # Stable selector using button text
        selector = 'button:has-text("Move to Testing User")'
        # Wait until button is visible
        self.page.wait_for_selector(selector, state="visible", timeout=15000)
        # Scroll into view in case it’s offscreen
        self.page.eval_on_selector(selector, "el => el.scrollIntoView()")
        # Click the button
        self.page.click(selector)

    def title(self):
        return self.page.title()
