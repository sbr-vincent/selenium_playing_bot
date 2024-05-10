from selenium import webdriver
from selenium.webdriver.common.by import By

# webdriver will be the thing that helps us automate tasks in the browser

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# The driver is sending the required headers that a website like Amazon would want.
driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/Bleach-Box-Set-Vol-1-21/dp/1421526107/ref=sr_1_1?crid=3RFPOKW63EXOJ&dib=eyJ2IjoiMSJ9.gb2c7xHvl4_pjZ_LMHc05A07C9pBebcNU-o7MLQUNJS7Jwby66DF1nFsn3DsPXBBg0tcDA6-eYwNlSSq8125C8AglP2OOfijss7vILUeftbfACUJgjaQgLwkysMqIGOi6bkbCS-ey70oOYmdUXcUaDgL9s7HiS_a70KxN92eTWQ6oeLVCHJ_yugxAqy-FQxcy2U8Xm8R0t8E5a49OTHOoLScqjVeJK0rBfHgeYN8-1s.dOLftQNF7BX8xzrttIk1dhDndLfpwKTDdIMz4uPQWIk&dib_tag=se&keywords=bleach+box+set&qid=1714507047&sprefix=bleach+bo%2Caps%2C129&sr=8-1")
# driver.implicitly_wait(15)
# price_dollar = driver.find_element(by="class name", value="a-price-whole").text
# price_cents = driver.find_element(by="class name", value="a-price-fraction")
# print(f"The price is {price_dollar}.{price_cents.text}")

driver.get("https://www.python.org/")
search_bar = driver.find_element(by="name", value="q")
# print(search_bar.tag_name) # returns the tag of the element
# print(search_bar.get_attribute("placeholder")) # returns the value of the attribute that we specify
# button = driver.find_element(by="id", value="submit")
# print(button.size)

# Can use the css selector to grab an element that doesn't have a class or an id
# documentation_link = driver.find_element(by="css selector", value=".documentation-widget a")
# print(documentation_link.text)

# Can use XPath to grab the element that we are looking for. click on the element and copy XPath and then you can use that in the find_element
# bug_link = driver.find_element(by="xpath", value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# Grabbing the Upcoming Dates On the Python.org page
# The line below grabs all the times and names
# upcoming_events = driver.find_elements(by="xpath", value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

event_times = driver.find_elements(by="css selector", value=".event-widget time")
event_names = driver.find_elements(by="css selector", value=".event-widget li a")

events_dict = {}

for n in range(len(event_times)):
    events_dict[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events_dict)


# Close will close the tab
# driver.close()
# Quit will close the entire program
driver.quit()
