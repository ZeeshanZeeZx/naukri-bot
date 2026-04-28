from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    # Use Firefox (better for stealth)
    browser = p.firefox.launch(headless=False)
    context = browser.new_context(
        viewport={'width': 1280, 'height': 720},
        locale='en-IN',
        timezone_id='Asia/Kolkata'
    )
    page = context.new_page()
    
    page.goto("https://www.naukri.com/nlogin/login")
    print("👉 Login manually within 60 seconds...")
    time.sleep(60)
    
    context.storage_state(path="state.json")
    print("✅ state.json saved")
    browser.close()