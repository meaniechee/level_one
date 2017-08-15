from selenium import webdriver

# Open the firefox browser
browser = webdriver.Firefox()

# Go to url
browser.get("https://moogoo.com.au")

storeelement = browser.find_element_by_css_selector('.nav > li:nth-child(2) > a:nth-child(1)') # assigning CSS selector to variable
storeelement.click()

newsletterele = browser.find_element_by_css_selector('#liteEMAILB')
newsletterele.send_keys('sam.kh@mailinator.com')
newsletterele.submit()