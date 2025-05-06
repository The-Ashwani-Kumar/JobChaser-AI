from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Set to False for a visible browser window
    page = browser.new_page()
    page.goto("https://www.linkedin.com")
    print("Loaded LinkedIn!")
    browser.close()
