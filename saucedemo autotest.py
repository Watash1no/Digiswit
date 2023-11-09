import os
import random
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# chek if site opens
os.environ['PATH'] += r"/usr/local/bin"
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(5)

if driver.current_url != "https://www.saucedemo.com/":
    print("Open site - fail")
else:
    print("Open site - pass")

driver.quit()

# login with no name
os.environ['PATH'] += r"/usr/local/bin"
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(5)

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username.send_keys("")
password.send_keys("1")

login_button.click()

try:
    error_message = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CLASS_NAME, "error-button"))
    )
    print("No User name - pass", error_message.text)
except Exception as e:
    print(" No user name - fail")
driver.quit()

# login with no password
os.environ['PATH'] += r"/usr/local/bin"
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(5)

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username.send_keys("1")
password.send_keys("")

login_button.click()

try:
    error_message = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CLASS_NAME, "error-button"))
    )
    print("No Password - pass", error_message.text)
except Exception as e:
    print(" NO Password - fail")
driver.quit()

# successful login

os.environ['PATH'] += r"/usr/local/bin"
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(5)

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")

login_button.click()

if driver.current_url != "https://www.saucedemo.com/inventory.html":
    print("Login - fail")
else:
    print("Login - pass")

# buy button, cart icon appear

buy_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
buy_button.click()

cart_icon = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge"))
)
if cart_icon:
    print("Сart icon - pass")

#open cart, product present

cart_button = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
cart_button.click()

current_url = driver.current_url
expected_url = "https://www.saucedemo.com/cart.html"

if current_url == expected_url:
    print("Cart page - pass")
else:
    print("Cart page - fail")

try:
    cart_item = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart_item")))
    item_name = cart_item.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
except TimeoutException:
    print("Item present - fail")
else:
    if item_name is not None:
        print("Item present - pass")
    else:
        print("Item present - fail")

#checkout, moving to right place

checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()

current_url = driver.current_url
expected_url = "https://www.saucedemo.com/checkout-step-one.html"

if current_url == expected_url:
  print("Checkout page - pass")
else:
  print("Checkout page - fail")

#first name fill in
first_names = ["John", "Jane", "Peter", "Mary", "David", "Elizabeth"]
first_name = first_names[random.randint(0, len(first_names) - 1)]

first_name_input = driver.find_element(By.ID, "first-name")
first_name_input.send_keys(first_name)

first_name_value = first_name_input.get_attribute("value")
if first_name == first_name_value:
  print("First name - pass")
else:
  print("First name - fail")

#last name fill in
last_names = ["Smith", "Brown", "Jones", "Williams", "Davis"]
last_name = last_names[random.randint(0, len(last_names) - 1)]

last_name_input = driver.find_element(By.ID, "last-name")
last_name_input.send_keys(last_name)

last_name_value = last_name_input.get_attribute("value")
if last_name == last_name_value:
  print("Last name - pass")
else:
  print("Last name - fail")

#postal code fill in
postal_codes = ["12345", "54321", "98765", "43210", "21043"]
postal_code = postal_codes[random.randint(0, len(postal_codes) - 1)]

postal_code_input = driver.find_element(By.ID, "postal-code")
postal_code_input.send_keys(postal_code)

postal_code_value = postal_code_input.get_attribute("value")
if postal_code == postal_code_value:
  print("Postal code - pass")
else:
  print("Postal code - fail")

#continue, check site
continue_button = driver.find_element(By.ID, "continue")

continue_button.click()

current_url = driver.current_url
if current_url == "https://www.saucedemo.com/checkout-step-two.html":
  print("Checkout Step Two - pass")
else:
  print("Checkout Step Two - fail")

#finish, site check, complete check
finish_button = driver.find_element(By.ID, "finish")
finish_button.click()

current_url = driver.current_url
if current_url == "https://www.saucedemo.com/checkout-complete.html":
  print("Checkout Complete - pass")
else:
  print("Checkout Complete - fail")

text = driver.find_element(By.CSS_SELECTOR, "span.title").text
if text == "Checkout: Complete!":
  print("Complete! - pass")
else:
  print("Complete!- fail")

#back to home
back_to_products_button = driver.find_element(By.ID, "back-to-products")

back_to_products_button.click()

current_url = driver.current_url
if current_url == "https://www.saucedemo.com/inventory.html":
  print("Home - pass")
else:
  print("Home - fail")