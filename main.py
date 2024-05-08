from selenium import webdriver
from selenium.webdriver.common.by import By

# webdriver will be the thing that helps us automate tasks in the browser

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Bleach-Box-Set-Vol-1-21/dp/1421526107/ref=sr_1_1?crid=3RFPOKW63EXOJ&dib=eyJ2IjoiMSJ9.gb2c7xHvl4_pjZ_LMHc05A07C9pBebcNU-o7MLQUNJS7Jwby66DF1nFsn3DsPXBBg0tcDA6-eYwNlSSq8125C8AglP2OOfijss7vILUeftbfACUJgjaQgLwkysMqIGOi6bkbCS-ey70oOYmdUXcUaDgL9s7HiS_a70KxN92eTWQ6oeLVCHJ_yugxAqy-FQxcy2U8Xm8R0t8E5a49OTHOoLScqjVeJK0rBfHgeYN8-1s.dOLftQNF7BX8xzrttIk1dhDndLfpwKTDdIMz4uPQWIk&dib_tag=se&keywords=bleach+box+set&qid=1714507047&sprefix=bleach+bo%2Caps%2C129&sr=8-1")
driver.implicitly_wait(15)
price_dollar = driver.find_element(by="class name", value="a-price-whole").text
price_cents = driver.find_element(by="class name", value="a-price-fraction")
print(f"The price is {price_dollar}.{price_cents.text}")


# Close will close the tab
# driver.close()
# Quit will close the entire program
driver.quit()
