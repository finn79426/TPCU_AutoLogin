
from selenium import webdriver
import os
import sys
import time

# 初始化
print("啟動中...\n")
# 尋找是否有config.py | config.txt
try:
    configfile = os.rename('config.txt','config.py')
except FileNotFoundError:
    if os.path.exists('config.py'):
        pass
    else:
        print('找不到config.txt！\n請重新建立一個')
        sys.exit()
import config
time.sleep(1)


# 定位webdriver
chromedriver = config.PATH
os.environ['webdriver.chrome.driver'] = chromedriver
driver = webdriver.Chrome(chromedriver)

# 打開driver,前往指定位子
driver.get('http://siw71.tpcu.edu.tw/tsint/')
# 載入後等 X 秒
driver.implicitly_wait(2)



# 自動驗證碼
# driver.execute_script("var not_CAPTCHA")
driver.execute_script("not_CAPTCHA = eval(window.frames[2].document.querySelectorAll('font')[6].innerText.replace(/=/, ''));")
driver.execute_script("window.frames[2].document.querySelector('#ls_chkrand').value = not_CAPTCHA;")
##### 特別感謝黑黑ZoneTwelve提供JavaScript Code給小弟 <(_ _)>  #####


# 跳轉到 Main frame
frame = driver.find_element_by_id("Main")
driver.switch_to_frame(frame)
# 搜索元素
username = driver.find_element_by_name("uid")
passwd = driver.find_element_by_name('pwd')

# keyin
username.send_keys(config.Username)
passwd.send_keys(config.Password)


# 登入成功
driver.find_element_by_id("chk").click()
print("登入成功！\nMade by：小曹\n有問題請來信：finn79426@gmail.com")
