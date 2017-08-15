from selenium import webdriver
import time


# Open the firefox browser
browser = webdriver.Firefox()

# Go to URL
browser.get('https://www.123rf.com')

# Go to signup page
signup_button = browser.find_element_by_css_selector('.header-bar-right > div:nth-child(3) > a:nth-child(1) > div:nth-child(1)')
signup_button.click() 

# Sleep for n seconds while waiting for browser to load
# time.sleep(2)

username_field = browser.find_element_by_css_selector('#panel_field_newuid')
username_field.send_keys('testerinokappachino')

email_field = browser.find_element_by_css_selector('#panel_field_newemail')
email_field.send_keys('rarara@gmail.com')

password_field = browser.find_element_by_css_selector('#panel_field_newpassword')
password_field.send_keys('12-eeVVdstZ')



'''
gdocs_file = open("gdocs.txt","r")
gdocs_info = gdocs_file.readlines()
gid = gdocs_info[month]
gdocs_file.close() #Close text file
'''