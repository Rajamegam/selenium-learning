import time

from selenium import webdriver

"""
1.Running the automation script in headless mode where browser will not invoke and run in headless mode
2. .ChromeOptions --> class to declare the options in chrome
3. .add_argument("headless") --> need to tell the browser to invoke in headless mode and we need to tell the same while
invoking the browser like this --> driver= webdriver.Chrome(options=chromeoptions)
5. to handle certification (SSL) errors -->options.add_argument("--ignore-certificate-errors") 
6 . to start the browser in maximized mode --> options.add_argument("--start-maximized")
"""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

"""
.execute_script() --> used to execute js based actions on the web page
window.scrollBy(0,document.body.scrollHeight)--> is used to go to the bottom of the page
.scrollHeight --> will take the maximum height of the page and scroll to that position
"""
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
# to take screenshot -> here it will scroll to the end of the page and take screenshot
driver.get_screenshot_as_file("screen.png")
print(driver.title)
time.sleep(2)
