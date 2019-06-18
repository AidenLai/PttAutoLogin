# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 04:00:14 2019

@author: minto
"""

import telnetlib
import sys
import time

host = 'ptt.cc'
user = 'USER'
password = 'PSWD'


telnet = telnetlib.Telnet(host)
time.sleep(1)
content = telnet.read_very_eager().decode('big5','ignore')
print(content)

if u"請輸入代號" in content:
    print("輸入帳號中...")
    telnet.write((user + "\r\n").encode('big5'))
    time.sleep(1)
    
    content = telnet.read_very_eager().decode('big5','ignore')

    print(content)

    if u"請輸入您的密碼" in content:
        print("輸入密碼中...")
        telnet.write((password + "\r\n").encode('big5') )
        time.sleep(1)

        content = telnet.read_very_eager().decode('big5','ignore')

        print(content)

        if u"您想刪除其他重複登入的連線嗎" in content:
            print("不刪除其他登入...")
            telnet.write(("n\r\n").encode('big5'))
            time.sleep(1)
            content = telnet.read_very_eager().decode('big5','ignore')
            print(content)

            if u"請按任意鍵繼續" in content:
                print("資訊頁面，按任意鍵繼續...")
                telnet.write(("\r\n").encode('big5') )
                time.sleep(2)
                content = telnet.read_very_eager().decode('big5','ignore')
                print(content)