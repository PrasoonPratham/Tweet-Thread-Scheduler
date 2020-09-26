import yaml
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

link = "https://twitter.com"
driver.get(link)

# make variables username and password, then set them to the credentials of your twitter account

signIn = "/html/body/div/div/div/div/main/div/div/div/div[1]/div/a[2]/div"
logIn = "/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div"

usernameBox = "/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input" 
passwordBox = "/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input"

#Login Sequence
signInButton = driver.find_element_by_xpath(signIn)
signInButton.click()

signInEmailId = driver.find_element_by_xpath(usernameBox)
signInEmailId.send_keys(username)

signInPass = driver.find_element_by_xpath(passwordBox)
signInPass.send_keys(password)

logInButton = driver.find_element_by_xpath(logIn)
logInButton.click()

#Tweet sequence
tweetButton = '/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'

tweet = driver.find_element_by_xpath(tweetButton)
tweet.click()

tweet = driver.find_element_by_xpath(tweetButton)
tweet.click()