TPCU_AutoLogin
===========================
自動登入 台北城市科技大學校務資訊系統
****
### Author:小曹(曹富翔)
### E-mail:finn79426@gmail.com
****

# 這是什麼？

這是一款利用JavaScript寫的腳本。  
可以讓你在造訪校務資訊系統登入頁面時，就幫你自動打上驗證碼，甚至可以達到自動登入的工具。

# 準備

由於此腳本是掛在瀏覽器上運行，首先您必須要有網頁瀏覽器

再來，你需要安裝Tampermonkey瀏覽器插件
- GoogleChrome用戶，[請點我安裝](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo)
- FireFox用戶，[請點我安裝](https://addons.mozilla.org/zh-TW/firefox/addon/tampermonkey/)
- Safari用戶，[請點我安裝](http://tampermonkey.net/?browser=safari)
- Opera用戶，[請點我安裝](https://addons.opera.com/zh-tw/extensions/details/tampermonkey-beta/?display=en)
- Microsoft Edge用戶，[請點我安裝](https://www.microsoft.com/zh-tw/store/p/tampermonkey/9nblggh5162s?rtc=1)


# 如何使用

以下以Google Chrome V63.0.3239 做示範

在下載好插件後，請到 [這裡](https://greasyfork.org/zh-TW/scripts/37838-tpcu-autologin) 下載腳本。

點擊"安裝腳本"<br><br>
![](https://i.imgur.com/QwZJF3L.png)
<br>
點擊"安裝"<br><br>
![](https://i.imgur.com/P641UDA.png)
<br>
畫面會閃一下，然後關閉  
點擊瀏覽器右上角Tampermonkey的圖示，並點選"控制台"<br><br>
![](https://i.imgur.com/QHefBhc.png)
<br>
若看到已啟用的部份是綠色的，就代表安裝完成囉 (未啟用是灰色)<br><br>
![](https://i.imgur.com/OgqCGwv.png)
<br>
這個時候只要去 [校務資訊系統](http://www.siw.tpcu.edu.tw/tsint/) 看看驗證碼有沒有自動幫你算出來就完成囉
<br>

# 進階-自動登入

請先進入 Tampermonkey 的控制台<br><br>
![](https://i.imgur.com/QHefBhc.png)
<br><br>
對TPCU_AutoLogin的最右邊，點選編輯<br><br>
![](https://i.imgur.com/gBWEwIJ.png)
<br><br>

請先詳細閱讀<font color=red>使用注意事項</font>再決定是否啟用自動登入功能。

若要使用自動登入功能，請將程式碼改成如下列範例：

```javascript=
/* 自動登入設定 */
var auto_login = "true"; // 若要啟用自動登入功能，將"false"改為"true"

/* 若不啟用自動登入功能，以下免填 */
var username = "s50431107";        // 在雙引號裡填入你的帳號
var password = "VerySecure";        // 在雙引號裡填入你的密碼
```

# 特別感謝

特別感謝ZoneTwelve提供JavaScript Code給小弟我<br>
沒有你，我完成不了驗證碼的部分，因為我不會寫JS :sweat_smile: 
<(_ _)>

# ToDo

* 新增快速請假
* 新增自動選課
* 新增暴力加選

# 免責說明

本程式並不會盜用您任何個資<br>
原始碼都公開出來了，也沒得盜<br>
若不放心，請勿使用<br>
<br>
禁止將此程式用作不法用途<br>
此程式套用 CC-BY-SA
