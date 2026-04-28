from playwright.sync_api import sync_playwright
import random

headlines = [
    "Python Developer with 3+ years building web apps and optimizing databases. Skilled in full-stack development, scalable architecture, AI and Agentic AI solutions, and cloud platforms to deliver secure, high-performance systems.",
    "Experienced Python Developer with 3+ years in web development and DB optimization. Proficient in full-stack systems, scalable design, AI and Agentic AI workflows, and cloud technologies for reliable, efficient applications.",
    "Results-driven Python Developer with 3+ years in web and database optimization. Builds scalable apps using full-stack tech, AI and Agentic AI capabilities, and cloud-native architectures with agile practices.",
    "Python Developer with 3+ years of experience in dynamic web applications. Expertise in full-stack development, database tuning, scalable systems, AI and Agentic AI integration, and cloud-based deployments.",
    "Full-stack Python Developer with 3+ years building web applications. Skilled in database management, scalable design, AI and Agentic AI solutions, and cloud environments with agile delivery.",
    "Innovative Python Developer with 3+ years in web development. Specializes in database optimization, scalable architecture, AI and Agentic AI systems, and cloud platforms for high-performance apps.",
    "Python Developer with 3+ years in web app development. Skilled in full-stack engineering, database tuning, scalable design, AI and Agentic AI solutions, and cloud-based application delivery.",
    "Dedicated Python Developer with 3+ years building and optimizing web apps. Expertise in full-stack development, database performance, scalable systems, AI and Agentic AI, and cloud infrastructure."
]

def update_naukri_headline():
    print("🚀 Script started")
    
    with sync_playwright() as p:
        # Use Firefox (harder to detect) with headless mode
        browser = p.firefox.launch(
            headless=True,
            args=['--disable-blink-features=AutomationControlled']
        )
        
        # Create context with realistic settings
        context = browser.new_context(
            storage_state="state.json",
            viewport={'width': 1280, 'height': 720},
            user_agent="Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
            locale='en-IN',
            timezone_id='Asia/Kolkata'
        )
        
        page = context.new_page()
        
        # Remove automation flags manually (for Firefox)
        page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
            Object.defineProperty(navigator, 'plugins', {get: () => [1,2,3,4,5]});
            Object.defineProperty(navigator, 'languages', {get: () => ['en-IN', 'en']});
        """)
        
        print("🌐 Navigating to profile...")
        page.goto("https://www.naukri.com/mnjuser/profile", wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(5000)
        
        print(f"📄 Page title: {page.title()}")
        
        if "Access Denied" in page.title():
            print("❌ Access Denied – saving screenshot")
            page.screenshot(path="debug_denied.png")
            browser.close()
            return
        
        # Click pencil
        print("🔍 Clicking pencil...")
        pencil = page.locator("span.edit.icon")
        if pencil.count() == 0:
            print("⚠️ Pencil not found. Saving screenshot.")
            page.screenshot(path="no_pencil.png")
            browser.close()
            return
        
        pencil.first.click()
        page.wait_for_timeout(1000)
        
        headline = random.choice(headlines)
        print(f"📝 New headline: {headline[:60]}...")
        
        # Fill textarea
        textarea = page.locator("textarea")
        textarea.fill(headline)
        
        # Click Save button
        print("💾 Clicking Save button...")
        save_button = page.locator("button.btn-dark-ot[type='submit']")
        if save_button.count() == 0:
            save_button = page.locator("button:has-text('Save')")
        
        if save_button.count() > 0:
            save_button.first.click()
            print("✅ Save button clicked")
        else:
            print("⚠️ Save button not found, pressing Enter")
            textarea.press("Enter")
        
        page.wait_for_timeout(5000)
        print("🎉 Headline updated successfully!")
        
        # Take final screenshot to verify
        page.screenshot(path="success.png")
        browser.close()

if __name__ == "__main__":
    update_naukri_headline()