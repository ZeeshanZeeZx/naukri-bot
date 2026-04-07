import random
import time
import pickle

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 🔹 Your headline list
HEADLINES = [
    "Python Developer with 3+ years of experience in building web applications and optimizing databases. Skilled in full-stack development, scalable architecture, and agile methodologies to deliver efficient, secure solutions.",
    
    "Experienced Python Developer with 3+ years in web app development and database optimization. Proficient in full-stack development, scalable architecture, and agile workflows to ensure high-performance solutions.",
    
    "Results-driven Python Developer with 3+ years in web development and database optimization. Adept at building scalable applications using full-stack technologies and agile methodologies.",
    
    "Python Developer with expertise in full-stack development, database optimization, and scalable architecture. Plus 3 years of experience in building dynamic, high-performance web applications.",
    
    "Full-stack Python Developer with 3+ years of experience in developing web applications. Skilled in database management, scalable system design, and agile-driven development.",
    
    "Innovative Python Developer with 3+ years in web development. Specializes in database tuning, full-stack development, and scalable architecture for high-performance apps.",
    
    "Python Developer with 3+ years in web app development. Skilled in full-stack development, database tuning, and scalable design to build efficient, agile-driven applications.",
    
    "Dedicated Python Developer with 3+ years of experience in building and optimizing web applications. Expertise in full-stack development, database performance, and scalable architecture."
]


def update_naukri():
    try:
        # 🔹 Chrome options
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")

        # 🔹 Start browser
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        # STEP 1: Open base site
        driver.get("https://www.naukri.com")
        time.sleep(3)

        # STEP 2: Load cookies
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        print("✅ Cookies loaded")

        # STEP 3: Open profile page
        driver.get("https://www.naukri.com/mnjuser/profile")
        time.sleep(5)

        wait = WebDriverWait(driver, 15)

        # STEP 4: Click edit (pencil icon)
        try:
            pencil = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'edit') and contains(text(),'editOneTheme')]"))
            )
            pencil.click()
            print("✏️ Clicked pencil icon")
        except:
            print("❌ Pencil icon not found.")
            driver.quit()
            return

        time.sleep(2)

        # STEP 5: Find textarea
        try:
            textarea = driver.find_element(By.ID, "resumeHeadlineTxt")
        except:
            print("❌ Textarea not found.")
            driver.quit()
            return

        # STEP 6: Pick random headline
        new_headline = random.choice(HEADLINES)

        # STEP 7: Replace text
        textarea.clear()
        time.sleep(1)
        textarea.send_keys(new_headline)

        print("✏️ New headline:", new_headline)

        # STEP 8: Click Save
        try:
            save_btn = driver.find_element(By.XPATH, "//button[text()='Save']")
            save_btn.click()
        except:
            print("❌ Save button not found.")
            driver.quit()
            return

        print("✅ Headline updated successfully!")

        time.sleep(5)
        driver.quit()

    except Exception as e:
        print("🔥 ERROR:", str(e))


if __name__ == "__main__":
    update_naukri()