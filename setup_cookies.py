import time
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://www.naukri.com/nlogin/login")

print("👉 Login manually within 60 seconds...")

time.sleep(60)  # Give enough time

# 🔥 Check before saving
cookies = driver.get_cookies()

if not cookies:
    print("❌ No cookies found. Login may have failed.")
else:
    pickle.dump(cookies, open("cookies.pkl", "wb"))
    print("✅ Cookies saved successfully!")

driver.quit()