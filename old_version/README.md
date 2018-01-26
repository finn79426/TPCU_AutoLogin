TPCU_AutoLogin
===========================
自動登入 台北城市科技大學校務資訊系統
****
### Author:小曹(曹富翔)
### E-mail:finn79426@gmail.com
****
# 目錄
* [Getting Started](#開始)
* [Code Example](#代碼說明)
* [How to Install?](#如何安裝？)
* [How to Setup?](#如何設定？)
* [How to run?](#如何使用？)
* [How to edit config again?](#如何修改設定？)
* [特別感謝](#特別感謝)
* [免責說明](#免責說明)


## 開始
你至少需要：
* Windows 64bit 或是 任意Linux發行版64bit
* Clone 或是 dowload **TPCU_AutoLogin**
* Python3.5
* Chrome安裝版 (請先事前安裝完成)

## 代碼說明
```
config.txt : 設定檔，需在裡面設定帳號、密碼等
login.py : 主程式，內有處理驗證碼，尋找元素的code
Linux_chrome : Linux用的webdriver，binary檔案
Windows_chrome.exe : Windows用的webdriver，exe檔案
```

## 如何安裝？
首先，請先到 www.python.org 下載Python<br>
請至少選擇3.5以上的版本，並請在安裝過程勾選安裝pip
![](https://i.imgur.com/Hsf0GSb.png)
![](https://i.imgur.com/3GLfvxu.png)

安裝完成後，打開你的終端機介面

windows使用者按下Win鍵，輸入cmd後Enter<br>
Linux使用者打開Terminal<br>
輸入：
```
pip install selenium
```
![](https://i.imgur.com/Wxr3Ybg.png)

過程中他會安裝一些套件，等他跑完就好了

## 如何設定？
**打開 config.txt，將chrome路徑、帳號、密碼輸入進去**<br>
<br>
這邊要注意的是，<font color="red">路徑是指driver的路徑</font><br>
如果你是Windows用戶，那就使用Windows_chrome.exe<br>
如果你是Linux用戶，那就使用Linux_chrome<br>
**請將路徑帳號密碼包在引號裡面！**

<font color="red">**windows用戶請注意，請依照下圖使用的格式**</font>
![](https://i.imgur.com/FJXvamI.png)

以作者的windows環境來說:
```
PATH = 'C:/Users/user/Desktop/tpcu/Windows_chrome.exe'
Username = 'myusername'
Password = 'mypassword'
```
以作者的Linux環境來說:
```
PATH = '/home/coolman/tpcu/Linux_chrome'
Username = 'myusername'
Password = 'mypassword'
```

## 如何使用？
再次打開終端機介面(參考[如何安裝?](#如何安裝？))<br>
使用 cd 指令切換到 login.py 的資料夾

![](https://i.imgur.com/bc3c2ap.png)

輸入
```
python login.py
```
看到這個畫面就代表成功囉
![](https://i.imgur.com/mhBfmZg.png)

**9/14更新**
Windows用戶僅需雙擊start.bat即可啟動
Linux尚無，因為我不會寫shell script XDD

## 如何修改設定？
config.txt即會被轉成.py檔案<br>
若要修改config內容，可刪除config.py再新增一個config.txt即可<br>
也可以直接修改config.py (如果你會的話)

## 特別感謝
特別感謝ZoneTwelve提供JavaScript Code給小弟我<br>
沒有你，我完成不了驗證碼的部分，因為我不會寫JS :sweat_smile: 
<(_ _)>

## ToDo
* 支援IE (天殺的學校阿....)
* 新增快速請假
* 新增自動選課
* 新增暴力加選

## 免責說明
本程式並不會盜用您任何個資<br>
原始碼都公開出來了，也沒得盜<br>
若不放心，請勿使用<br>
<br>
禁止將此程式用作不法用途<br>
此程式套用 CC-BY-SA
