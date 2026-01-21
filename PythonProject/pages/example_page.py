from playwright.sync_api import Page


class ExamplePage:
    URL = "https://office.carteav.com"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def click_move_to_testing_user(self):
        selector = 'button:has-text("DEMO USER 1")'
        self.page.wait_for_selector(selector, state="visible", timeout=15000)
        self.page.eval_on_selector(selector, "el => el.scrollIntoView()")
        self.page.click(selector)
        print("➡ Clicked 'Move to Testing User'")

    def open_poi_dropdown(self):
        selector = ".topLeftActionsButtonsContainer > div:first-child"
        self.page.wait_for_selector(selector, timeout=15000)
        self.page.evaluate(
            """(selector) => {
                document.querySelector(selector).click();
            }""",
            selector
        )
        print("📂 Opened POI dropdown")

    def click_move_to_spa_sababa(self):
        selector = '#pois_items > div > div:nth-child(6) > div.poi_poiTextContainer__V4Q1q > div > div'
        self.page.wait_for_selector(selector, state="visible", timeout=15000)
        self.page.eval_on_selector(selector, "el => el.scrollIntoView()")
        self.page.click(selector)
        print("➡ Clicked 'Spa sababa'")

    def click_order_vehicle(self):
        # Click the "הזמן רכב" button by visible text
        locator = self.page.locator('text=הזמן רכב')

        locator.wait_for(state="visible", timeout=15000)
        locator.scroll_into_view_if_needed()
        locator.click(force=True)

        print("➡ Clicked 'הזמן רכב'")

    def click_start_driving(self):
        # Click the "התחל נסיעה" button by visible text
        locator = self.page.locator('text=התחל נסיעה')

        locator.wait_for(state="visible", timeout=15000)
        locator.scroll_into_view_if_needed()
        locator.click(force=True)

        print("➡ Clicked 'התחל נסיעה'")

    def title(self):
        return self.page.title()
