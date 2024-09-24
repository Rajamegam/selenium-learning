import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver and maximize the window
driver = webdriver.Chrome()
driver.maximize_window()

# Expected product name
expected_product = ["Amazon Brand - Solimo Round Analog Wall Clock|Plastic|10 Inch|Black"]
actual_product_list = []

# Navigate to Amazon
driver.get("https://amazon.in")
action = ActionChains(driver)

# Search for "wall clock"
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("wall clock")
driver.find_element(By.ID, "twotabsearchtextbox").send_keys(Keys.ENTER)

# Wait for the search results to load
wait = WebDriverWait(driver, 10)
search_list = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".a-section.a-spacing-base")))

# Iterate over each product in the search results
for product in search_list:
    product_name_element = product.find_element(By.XPATH,
                                                "//div[@class='a-section a-spacing-small puis-padding-left-small puis-padding-right-small']/div/h2/a/span")
    product_name = product_name_element.text
    actual_product_list.append(product_name)

    # Check if the current product matches the expected product
    if expected_product[0] in actual_product_list:
        print(f"Product found: {product_name}")

        # Scroll to the product and click on the product link (not "Add to Cart" yet)
        product_name_element.click()
        break

print("Products found:", actual_product_list)

# Give time to see the results, it's better to use waits instead of sleep in real code
time.sleep(5)

# Close the browser
driver.quit()
