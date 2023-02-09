from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.csie.ntu.edu.tw/~b01902112/9007199254740992/')

action = ActionChains(driver)

# play the game
while True:
    action.send_keys(Keys.UP).perform()
    action.send_keys(Keys.RIGHT).perform()
    action.send_keys(Keys.DOWN).perform()
    action.send_keys(Keys.LEFT).perform()