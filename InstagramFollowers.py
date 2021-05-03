#Instagram followers check
#Coded by ultraviolex, 2020


import time
import getpass
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://instagram.com')
time.sleep(3)

loginForm = driver.find_element_by_id('loginForm')
usernameElement = loginForm.find_element_by_name('username')
username = input('Please enter account username: ')
usernameElement.send_keys(username)

passwordElement = loginForm.find_element_by_name('password')
password = getpass.getpass('Please enter account password: ')
passwordElement.send_keys(password)
password = ""

submitElement = loginForm.find_element_by_xpath("//button[@type='submit']")
submitElement.click()
time.sleep(3)

notNowElement = driver.find_element_by_xpath("//*[contains(text(), 'Not Now')]")
notNowElement.click()
time.sleep(3)

notNowElement = driver.find_element_by_xpath("//*[contains(text(), 'Not Now')]")
notNowElement.click()
time.sleep(3)

driver.get('https://instagram.com/{}'.format(username))
time.sleep(3)

followers = []
following = []
notFollowingBack = []

followersElement = driver.find_element_by_xpath("//a[@href='/{}/followers/']".format(username))
followersNumHTML = BeautifulSoup(followersElement.get_attribute('innerHTML'), 'html.parser')
followersNum = int(followersNumHTML.find('span').contents[0])
print(followersNum)
followersElement.click()
time.sleep(3)

followersWindow = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul")
try:
    followersWindow.click()
    time.sleep(1)
except StaleElementReferenceException:
    followersWindow = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul")
    followersWindow.click()
    time.sleep(1)

followersScroll = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
followersSoup = BeautifulSoup(followersWindow.get_attribute('innerHTML'), 'html.parser')
i = 100
while (len(followersSoup.find_all("li")) != followersNum):
    print(len(followersSoup.find_all("li")))
    try:
        driver.execute_script("arguments[0].scrollTop = arguments[1]", followersScroll, i)
    except StaleElementReferenceException:
        driver.back()
    i += 400
    time.sleep(2)
    followersSoup = BeautifulSoup(followersWindow.get_attribute('innerHTML'), 'html.parser')
    if (len(followersSoup.find_all("li")) == followersNum -1):
        break
    if (len(followersSoup.find_all("li")) >= followersNum ):
        break


followerSoup = BeautifulSoup(driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul").get_attribute("innerHTML"), "html.parser")
for i in followersSoup.find_all("li"):
    followers.append(i.contents[0].contents[0].contents[1].contents[0].contents[0].contents[0]['title'])

driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button").click()
time.sleep(1)

followingElement = driver.find_element_by_xpath("//a[@href='/{}/following/']".format(username))
followingNumHTML = BeautifulSoup(followingElement.get_attribute('innerHTML'), 'html.parser')
followingNum = int(followingNumHTML.find('span').contents[0])
followingElement.click()
time.sleep(3)

followingWindow = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul")
try:
    followingWindow.click()
    time.sleep(1)
except StaleElementReferenceException:
    followingWindow = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul")
    followingWindow.click()
    time.sleep(1)

followingScroll = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
followingSoup = BeautifulSoup(followingWindow.get_attribute('innerHTML'), 'html.parser')
i = 100
while (len(followingSoup.find_all("li")) != followingNum):
    print(len(followingSoup.find_all("li")))
    try:
        driver.execute_script("arguments[0].scrollTop = arguments[1]", followingScroll, i)
    except StaleElementReferenceException:
        driver.back()
    i += 400
    time.sleep(2)
    followingSoup = BeautifulSoup(followingWindow.get_attribute('innerHTML'), 'html.parser')


followingSoup = BeautifulSoup(driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul").get_attribute('innerHTML'), 'html.parser')
for i in followingSoup.find_all("li"):
    following.append(i.contents[0].contents[0].contents[1].contents[0].contents[0].contents[0]['title'])

print('Check to make sure the numbers are correct.')
print('Followers: ' + str(len(followers)))
print('Following: ' + str(len(following)))

for i in following:
    if i not in followers:
        notFollowingBack.append(i)

print('Users that are not following you back: ')
for i in notFollowingBack:
    print(i)

driver.close()
