from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import io
import sys
# import config
import time

# 定位webdriver
chromedriver = "/home/howpwn/桌面/form/chromedriver"
os.environ['webdriver.chrome.driver'] = chromedriver
driver = webdriver.Chrome(chromedriver)

# 打開driver,前往指定位子
driver.get('http://siw71.tpcu.edu.tw/tsint/')

# 載入後等 X 秒
driver.implicitly_wait(3)

# 跳轉frame
frame = driver.find_element_by_id("Main")
driver.switch_to_frame(frame)

# 搜索元素
username = driver.find_element_by_name("uid")
passwd = driver.find_element_by_name('pwd')

# keyin
username.send_keys('')
passwd.send_keys('')


randcode = driver.find_element_by_name('ls_chkrand')
randcode.send_keys('123')
