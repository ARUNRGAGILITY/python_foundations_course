from selenium import webdriver
from selenium.webdriver.common.by import By  # Import the By class
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Initialize the web driver (you need to have a web driver installed, e.g., ChromeDriver)
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://www.learnpythondjango.com")  # Replace with the URL of the website you're testing

# Wait for the link to become clickable
quiz_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Quiz']"))
)

# Click the link
quiz_link.click()

# driver.quit()
